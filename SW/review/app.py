import streamlit as st
import glob
import os
import pandas as pd 

def main():
    with st.sidebar: sidebar()
    contents()

def sidebar() :
    title =  '지역을 선택해주세요.'
    st.title(title)
    df = pd.concat([pd.read_csv(p) for p in sorted(glob.glob('/app/ml_project/SW/review/static/*.csv'))])    
    st.write(df)

def contents():
    pass

if __name__ == '__main__':
    main()
    st.write('hello :)')