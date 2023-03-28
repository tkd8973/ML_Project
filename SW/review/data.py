import pandas as pd
import streamlit as st
import glob

@st.cache_data
def read_data():
    glob_pt = '/app/ml_project/SW/review/static/*.csv'
    return pd.concat([pd.read_csv(p) for p in sorted(glob.glob(glob_pt))])  

def get_unique_list(data, index):
    return data.str.split(expand=True)[index].unique()

@st.cache_data
def get_city_list():
    df = read_data()
    return get_unique_list(df['시군구'], 0)

@st.cache_data
def get_gu_list(city_choice):
    df = read_data()
    return get_unique_list(df['시군구'][df['시군구'].str.contains(city_choice)], 1)