# Scripts
This folder contains Python scripts for data processing and Streamlit dashboard.
# Scripts README

## Streamlit Dashboard Development

### Development Process
1. Created a new branch `dashboard-dev` for the Streamlit app development.
2. Set up the folder structure:
   - `app/`: Contains `main.py` (Streamlit app) and `utils.py` (data processing functions).
   - `scripts/`: Contains this `README.md`.
3. Installed Streamlit via `pip install streamlit` and updated `requirements.txt`.
4. Developed `utils.py` to load and process cleaned datasets from `data/processed/`.
5. Developed `main.py` with:
   - A country selector widget using `st.multiselect`.
   - A boxplot of GHI distribution by country using `seaborn`.
   - A table of top regions by average GHI.
6. Tested the app locally using `streamlit run app/main.py`.

### Usage Instructions
1. Activate the virtual environment: