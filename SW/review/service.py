import streamlit as st
from data import read_data, check_contain

def get_filtered_data():
    df = read_data()
    ss = st.session_state
    city_choice, gu_choice, town_choice, village_choice = [
        ss[k] for k in ['city', 'gu', 'town', 'village']
    ]
    return df[
        check_contain(df['시군구'], city_choice),
        & check_contain(df['시군구'], gu_choice),
        & check_contain(df['시군구'], town_choice),
        & check_contain(df['시군구'], village_choice),
    ]
