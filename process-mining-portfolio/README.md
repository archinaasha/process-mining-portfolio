Process Mining Portfolio — Comparative Study & Event Log Analysis

This repository presents an independent, academically oriented portfolio project on Process Mining. It includes:

A comparative study of four representative tools: PM4Py, ProM, Celonis Academic, and Disco (covering open-source, academic, and commercial perspectives).

A case study event-log analysis using PM4Py (Google Colab–ready) with a publicly available dataset.

A website demo outline that illustrates how results can be communicated in a clear and user-friendly way (similar to public comparison portals).

Purpose:
To explore Process Mining tools and techniques from both technical and practical perspectives, while demonstrating skills in analysis, evaluation, visualization, and web presentation.

Capability Dimensions Used in the Comparison

The tools are evaluated along commonly discussed capability dimensions in Process Mining literature and practice:

Data Management

Process Discovery

Conformance Checking

Advanced Enhancement

Views / Monitoring / Reporting

Operational Support

Security & Compliance

Non-functional Qualities (e.g., usability, reliability, portability – inspired by ISO/IEC 25010)

These dimensions are consistently used in the comparison table and in the interpretation of case study results.

Repository Structure
process-mining-portfolio/
├─ README.md
├─ tool_comparison/
│  └─ comparison_table.md
├─ event_log_analysis/
│  ├─ pm4py_analysis.ipynb       # Google Colab–ready notebook
│  ├─ pm4py_analysis.py          # Script version (optional)
│  ├─ requirements.txt
│  └─ data/                      # Place event logs here (excluded via .gitignore)
├─ website_demo/
│  └─ README.md
├─ docs/
│  └─ placeholders.md            # Figures and summaries will be placed here
├─ .gitignore
└─ LICENSE

Datasets

Primary (commonly used and reproducible):

BPI Challenge 2017 (Order-to-Cash)

Optional (to provide additional insights or originality):

BPI Challenge 2012

Helpdesk Log

Road Traffic Fines Log

BPI Challenge 2020

Datasets can be added to event_log_analysis/data/ and referenced in the notebook or script.
