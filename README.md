# Process Mining Portfolio — Comparative Study & Event Log Analysis

This repository presents an independent, academically oriented portfolio project on **Process Mining**. It includes:

- A **comparative study** of four representative tools: **PM4Py, ProM, Celonis Academic, and Disco** (covering open-source, academic, and commercial perspectives).
- A **case study event-log analysis** using **PM4Py** (Google Colab–ready) with a publicly available dataset.
- A **website demo outline** that illustrates how results can be communicated clearly (similar to public comparison portals).

**Purpose:** Explore Process Mining tools and techniques from both technical and practical perspectives, while demonstrating skills in analysis, evaluation, visualization, and web presentation.

## Capability Dimensions Used in the Comparison
Tools are evaluated along commonly discussed capability dimensions:
1. Data Management
2. Process Discovery
3. Conformance Checking
4. Advanced Enhancement
5. Views / Monitoring / Reporting
6. Operational Support
7. Security & Compliance
8. Non-functional Qualities (e.g., usability, reliability, portability – inspired by ISO/IEC 25010)

These dimensions are used in the comparison table and in the interpretation of case study results.

## Repository Structure
```
process-mining-portfolio/
├─ README.md
├─ tool_comparison/
│  └─ comparison_table.md
├─ event_log_analysis/
│  └─ pm4py_analysis.ipynb
├─ docs/                       # Generated figures and summaries
├─ .gitignore
```
## Datasets
**Primary (reproducible):** BPI Challenge 2017 (Order-to-Cash)  
**Optional (to add breadth):** BPI 2012, Helpdesk, Road Traffic Fines, BPI 2020

Place datasets under `event_log_analysis/data/` when running locally, or upload/mount them in Colab.

## Quickstart (Colab)
1. Open `event_log_analysis/pm4py_analysis.ipynb` in Google Colab.
2. Upload or mount a log file (e.g., `/content/BPI2017.xes.gz`) and set the path in the notebook.
3. Run the notebook to compute: basic stats, process discovery, (optional) conformance, and KPIs.
4. Save the generated figures and summaries to `docs/` for versioning and presentation.

## Quickstart (Local, optional)
Create a virtual environment and run the notebook with your local Python/Jupyter setup if preferred.

## Next Steps
- Fill `tool_comparison/comparison_table.md` with initial observations for PM4Py, ProM, Celonis Academic, and Disco.
- Run the analysis on BPI 2017 and optionally one additional dataset to improve coverage.
- Export figures and a short summary to `docs/`, and reference them in the README and any website presentation.
