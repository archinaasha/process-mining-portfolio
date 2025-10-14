"""
PM4Py minimal event-log analysis script.
Usage:
  python pm4py_analysis.py --log_path path/to/eventlog.xes --outdir ../docs
"""
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="PM4Py mini analysis (discovery + KPIs)")
    parser.add_argument("--log_path", type=str, default="", help="Path to event log file (.xes/.csv)")
    parser.add_argument("--outdir", type=str, default="../docs", help="Directory to save outputs")
    args = parser.parse_args()

    if not args.log_path:
        print("[INFO] Please supply --log_path to a public event log (e.g., BPI2017.xes.gz).")
        return

    try:
        from pm4py.objects.log.importer.xes import importer as xes_importer
        from pm4py.algo.discovery.inductive import algorithm as inductive_miner
        from pm4py.statistics.traces.generic.log import case_statistics
        from pm4py.util import xes_constants
        from pm4py.visualization.process_tree import visualizer as pt_visualizer
        from pm4py.objects.conversion.process_tree import converter as pt_converter
        from pm4py.visualization.petri_net import visualizer as pn_visualizer
        from pm4py.algo.conformance.alignments.petri_net import algorithm as alignments
        from pm4py.objects.log.util import sampling
        import pm4py
    except Exception as e:
        print("[ERROR] PM4Py not installed. Run: pip install -r event_log_analysis/requirements.txt")
        print("Exception:", e)
        return

    outdir = Path(args.outdir); outdir.mkdir(parents=True, exist_ok=True)

    print(f"[INFO] Loading log: {args.log_path}")
    log = xes_importer.apply(args.log_path)

    # Basic stats
    num_events = sum(len(trace) for trace in log)
    num_cases = len(log)
    variants_count = case_statistics.get_variant_statistics(log)
    num_variants = len(variants_count)
    print(f"[STATS] Cases: {num_cases} | Events: {num_events} | Variants: {num_variants}")

    # Sample for speed if huge
    sampled_log = sampling.sample_log_random(log, 1000) if num_events > 50000 else log

    # Discovery
    process_tree = inductive_miner.apply_tree(sampled_log)
    gviz_tree = pt_visualizer.apply(process_tree)
    tree_png = outdir / "process_tree.png"
    pt_visualizer.save(gviz_tree, str(tree_png))

    net, im, fm = pt_converter.apply(process_tree)
    gviz_pn = pn_visualizer.apply(net, im, fm)
    pn_png = outdir / "petri_net.png"
    pn_visualizer.save(gviz_pn, str(pn_png))

    # Conformance (sample)
    sample_for_align = sampling.sample_log_random(log, 200) if num_cases > 200 else log
    aligned_traces = alignments.apply_log(sample_for_align, net, im, fm)
    avg_fitness = sum(a['fitness'] for a in aligned_traces) / len(aligned_traces)
    print(f"[CONF] Average fitness (sample): {avg_fitness:.3f}")

    # KPI: median case duration
    case_durations = case_statistics.get_all_casedurations(log, parameters={
        xes_constants.DEFAULT_TIMESTAMP_KEY: "time:timestamp"
    })
    median_duration = pm4py.statistics.util.common.median(case_durations)
    print(f"[KPI] Median case duration (seconds): {median_duration:.2f}")

    # Summary
    summary = outdir / "analysis_summary.md"
    with open(summary, "w", encoding="utf-8") as f:
        f.write("# Mini Event‑Log Analysis — Summary\n\n")
        f.write(f"- Cases: **{num_cases}**\n")
        f.write(f"- Events: **{num_events}**\n")
        f.write(f"- Variants: **{num_variants}**\n")
        f.write(f"- Average alignment fitness (sample): **{avg_fitness:.3f}**\n")
        f.write(f"- Median case duration (seconds): **{median_duration:.2f}**\n")
        f.write("\n## Figures\n")
        f.write("- Process tree: `process_tree.png`\n")
        f.write("- Petri net: `petri_net.png`\n")
    print(f"[OUT] Saved summary: {summary}")

if __name__ == "__main__":
    main()