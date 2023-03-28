import requests
import streamlit as st
import pandas as pd
import numpy as np
import os
import datetime

# import xgboost as xgb
# xgb_model = xgb.XGBRegressor()
count = 0

title = "🏢 반포자이 사조"
text = "(2022년 3월 - 2023년 2월)"

st.markdown(f"<div style='font-weight:bold; font-size:35px; text-align:center'>{title}</div>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align:center; font-size:20px'>{text}</div>", unsafe_allow_html=True)

st.markdown(f"<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)


df_apt1 = pd.read_csv('Data/아파트_매매__실거래가_20230321134107_1월.csv')
df_apt2 = pd.read_csv('Data/아파트_매매__실거래가_20230321134120_2월.csv')

df_apt1["거래금액(만원)"] = df_apt1["거래금액(만원)"].str.replace(",", "").astype(int) # 거래금액 컬럼의 쉼표를 제거하고 정수형으로 변환
df_apt1["평단가"] = (df_apt1["거래금액(만원)"] / df_apt1["전용면적(㎡)"]) / 3.3 # 평당가 계산하여 새로운 컬럼 추가

def col_(i):
    col1,col2 = st.columns([1, 1])
    with col1 :
        # column 1 에 담을 내용
        st.slider('전용 면적을 선택해 주세요', 0.0, 300.0,key =i)
        # st.write("전용 면적 ", area, '(㎡)을 선택하셨습니다.')

        st.markdown(f"<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)

        genre = st.radio(
            "거래 유형을 선택해 주세요 (중개거래, 직거래)",
            ('중개거래', '직거래'), key=12+i )

        st.markdown(f"<div style='margin-top: 25px; margin-right: 20px;'></div>", unsafe_allow_html=True)


    with col2 :
        # column 2 에 담을 내용
        st.slider('건축 년도를 선택해 주세요', min_value = 1940, max_value=2023,step=1,key=i+1)
        # st.write("건축 년도 ", year_of_construction, '년을 선택하셨습니다.')

        st.markdown(f"<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)

        if st.button('현재 금리 적용', key=23+i):
            today = datetime.date.today()
            st.write(f'{today}')
        else:
            today = datetime.date.today()

    if st.button('예측', key=34+i):
        st.write("아파트 실거래가 예측 값 입니다")
    else:
        st.write("")


with tab0:
    tab0.subheader("📈Linear Regression📈")
    st.markdown(f"<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
    col_(0)


with tab1:
    tab1.subheader("🤝KNN🤝")
    col_(2)
    
         
with tab2:
    tab2.subheader("🌲Decision Tree🌲")
    col_(4)

    
with tab3:
    tab3.subheader("🌳Random Forest🌳")
    col_(6)

with tab4:
    tab4.subheader("💪XGBoost💪")
    col_(8)


with tab5:
    tab5.subheader("⚡️LightGBM⚡️")
    col_(10)

with tab6:


    '''
    ### 집사조😋
    | 이름 | 역할 | 모델링 |
    | :---: | :---: | :---: |
    | 서상원 | **팀장**, 발표, 데이터 수집 및 전처리, Streamlit, ML | KNN |
    | 조성훈 | 데이터 수집 및 전처리, ML | Decision Tree |
    | 곽희범 | 데이터 수집 및 전처리, ML | Random Forest |
    | 이영미 | 데이터 수집 및 전처리, ML | LightGBM |
    | 한재원 | 발표, 데이터 수집 및 전처리, Streamlit, ML | XGBoost |
    | 박상원 | 데이터 수집 및 전처리, ML | Linear Regression |
    | 이영재 | 아이디어 제공 | |
    | 최용재 | 아이디어 제공, 정보제공 | |
    '''

    '''
    ---
    ### 
    * 데이터출처 : 국토교통부 실거래가 공개 시스템
    * 아파트 실거래가 2022년 3월 ~ 2023년 2월까지의 데이터 입니다.
    > [데이터 다운로드]("http://rtdown.molit.go.kr/")
    ---
    '''