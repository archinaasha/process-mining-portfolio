# Process Mining Portfolio — Comparative Study & Event Log Analysis

This repository presents a **neutral, academic-style** portfolio project on Process Mining. It includes:
- A **comparative study** of four tools: **PM4Py, ProM, Celonis Academic, Disco** (selected to span open‑source, academic, and industry)
- A **case study** event‑log analysis with **PM4Py** (Colab‑ready), using a public dataset
- A **website demo outline** to communicate results clearly (mirrors how a public comparison portal might be structured)

> Positioning: This is an independent portfolio/research project for learning and demonstration. It is not made for any single organization, yet it aligns naturally with typical Process Mining survey criteria used in academia and industry.

---

## Capability Dimensions Used in the Comparison

We evaluate tools along commonly referenced capability dimensions in Process Mining literature and practice:
1. Data Management
2. Process Discovery
3. Conformance Checking
4. Advanced Enhancement
5. Views / Monitoring / Reporting
6. Operational Support
7. Security & Compliance
(+ Non‑functional qualities such as usability, reliability, portability — inspired by ISO/IEC 25010.)

These dimensions are used consistently in the comparison table and in the case study interpretation notes.

---

## Repository Structure

```
process-mining-portfolio/
├─ README.md
├─ tool_comparison/
│  └─ comparison_table.md
├─ event_log_analysis/
│  ├─ pm4py_analysis.ipynb       # Colab-ready notebook
│  ├─ pm4py_analysis.py          # Script version
│  ├─ requirements.txt
│  └─ data/                      # Place event logs here (excluded by .gitignore)
├─ website_demo/
│  └─ README.md
├─ docs/
│  └─ placeholders.md
├─ .gitignore
└─ LICENSE
```

---

## Datasets

**Primary (common for reproducibility):**
- **BPI Challenge 2017** (Order-to-Cash)

**Optional (to stand out / triangulate):**
- **BPI Challenge 2012**
- **Helpdesk** log
- **Road Traffic Fines** log
- **BPI Challenge 2020**

Add your chosen log files under `event_log_analysis/data/` and reference them from the notebook/script.

---

## Quickstart

### A) Google Colab (recommended)
1. Open `event_log_analysis/pm4py_analysis.ipynb` in Colab.
2. Upload or mount the event log into `/content/event_log.xes` (or adjust the path in the notebook).
3. Run the cells to compute:
   - Basic statistics (cases, events, variants)
   - **Process Discovery** (Inductive Miner) → process tree & Petri net
   - (Optional) **Conformance** (alignments) on a small sample
   - KPIs (e.g., median case duration)
4. Download/save figures to include in `docs/` and your website demo.

### B) Local (Python)
```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r event_log_analysis/requirements.txt
python event_log_analysis/pm4py_analysis.py --log_path event_log_analysis/data/your_log.xes --outdir docs
```

---

## Publish
```bash
git init
git add .
git commit -m "Initial commit: process mining portfolio (tools + case study)"
git branch -M main
git remote add origin https://github.com/<your-username>/process-mining-portfolio.git
git push -u origin main
```
Then mirror highlights on your WordPress demo (see `website_demo/README.md`).

---

## Next Steps
- Fill `tool_comparison/comparison_table.md` (start with high-level entries; refine over time).
- Run the notebook/script with **BPI 2017** and optionally a second dataset to add originality.
- Export figures to `docs/` and reference them from README and WordPress.