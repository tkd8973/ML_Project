import pandas as pd
import streamlit as st
import glob

@st.cache_data
def read_data():
    glob_pt = '/app/ml_project/SW/review/static/*.csv'
    return pd.concat([pd.read_csv(p) for p in sorted(glob.glob(glob_pt))])  

@st.cache_data
def get_city_list():
    df = read_data()
    return df['시군구'].str.split(expand=True)[0].unique()