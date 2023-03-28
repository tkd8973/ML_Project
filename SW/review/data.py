import pandas as pd
import streamlit as st

@st.cache_data
def read_data():
    glob_pt = '/app/ml_project/SW/review/static/*.csv'
    return pd.concat([pd.read_csv(p) for p in sorted(glob.glob(glob_pt))])  