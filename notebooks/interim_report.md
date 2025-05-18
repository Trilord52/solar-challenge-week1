Interim Report for 10 Academy: Artificial Intelligence Mastery - Solar Data Discovery: Week 0 Challenge
Submitted by: Tinbite Yonas
Date: May 18, 2025
Task 1: Git & Environment Setup

Objective: Set up the project environment and repository for the solar data challenge.
Progress:
Created a GitHub repository at https://github.com/Trilord52/solar-challenge-week1.
Initialized a branch setup-task with at least 3 commits:
init: add .gitignore (configured to ignore data/, .csv, .ipynb_checkpoints/, etc.).
chore: venv setup and add requirements.txt (installed matplotlib==3.8.0, seaborn==0.13.2, scipy==1.13.1, pandas, numpy, and added to requirements.txt).
ci: add GitHub Actions workflow and project structure (added .github/workflows/ci.yml to run pip install -r requirements.txt and check Python version).


Set up a virtual environment (venv) and documented setup instructions in README.md.
Created a project structure with src/, notebooks/, scripts/, and tests/ directories, including __init__.py files.
Merged setup-task into main via a Pull Request (PR) titled “Setup Task: Initialize project with venv, CI, and structure”.
Verified CI workflow success in the GitHub Actions tab.


Status: Completed.

Task 2: Data Profiling, Cleaning & EDA

Objective: Profile, clean, and explore the solar datasets for Benin-Malanville, Sierra Leone (Bumbuna), and Togo (Dapaong QC) for comparison and region-ranking tasks.
Progress:
Benin-Malanville:
Created a branch eda-benin-malanville.
Developed notebooks/benin-malanville_eda.ipynb to perform:
Summary Statistics & Missing-Value Report: Used df.describe() and df.isna().sum(), flagged columns with >5% nulls.
Outlier Detection & Cleaning: Computed Z-scores for GHI, DNI, DHI, ModA, ModB, WS, WSgust, flagged |Z|>3, imputed missing values with median, exported to data/processed/benin-malanville_clean.csv.
Time Series Analysis: Line charts of GHI, DNI, DHI, Tamb vs. Timestamp, monthly averages with Viridis, Plasma, Magma, Cividis colorbars.
Cleaning Impact: Bar chart of average ModA, ModB pre/post-cleaning (Teal, Coral).
Correlation & Relationship Analysis: Heatmap with Inferno colorbar for GHI, DNI, DHI, TModA, TModB, scatter plots of WS, WSgust, WD vs. GHI, RH vs. Tamb/GHI (Forest Green, Dark Orchid, Crimson, Navy, Goldenrod).
Wind & Distribution Analysis: Wind rose using WindroseAxes with Viridis colorbar, histograms for GHI (Sky Blue), WS (Salmon).
Temperature Analysis: Scatter plots of RH vs. Tamb (Dark Green), RH vs. GHI (Dark Orange), with correlations.
Bubble Chart: GHI vs. Tamb, bubble size = RH, Viridis colorbar.


Merged into main after resolving build error (pywin32==310 removed from requirements.txt).


Sierra Leone (Bumbuna):
Created a branch eda-sierra_leone_bumbuna.
Developed notebooks/sierra_leone_bumbuna_eda.ipynb with the same analyses as above, adjusted for data/raw/sierra_leone.csv, exported cleaned data to data/processed/sierra_leone_clean.csv.
Committed and pushed to eda-sierra_leone_bumbuna.


Togo (Dapaong QC):
Created a branch eda-togo_dapaong_qc.
Developed notebooks/togo_dapaong_qc_eda.ipynb with the same analyses, adjusted for data/raw/togo.csv, exported cleaned data to data/processed/togo_dapaong_qc_clean.csv.
Committed and pushed to eda-togo_dapaong_qc.




Status: Completed for all three locations; pending cross-country comparison and bonus task.

Next Steps

Merge eda-sierra_leone_bumbuna and eda-togo_dapaong_qc into main.
Perform cross-country comparison of key metrics (e.g., average GHI, cleaning impact).
Explore bonus task with a Streamlit dashboard.

Repository

GitHub URL: https://github.com/Trilord52/solar-challenge-week1

