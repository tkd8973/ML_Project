import requests
import streamlit as st
import pandas as pd
import numpy as np
import os
# import xgboost as xgb
# xgb_model = xgb.XGBRegressor()


st.write(
    """
    ## 어려운 부동산 ^_^...
    ---
    """
)

# st.sidebar.title('선택해라')
# selected_region = st.sidebar.selectbox("행정구역 선택해라", city_lis
# )


df_apt1 = pd.read_csv('Data/아파트_매매__실거래가_1월.csv')


df_apt1["거래금액(만원)"] = df_apt1["거래금액(만원)"].str.replace(",", "").astype(int) # 거래금액 컬럼의 쉼표를 제거하고 정수형으로 변환
df_apt1["평당가"] = (df_apt1["거래금액(만원)"] / df_apt1["전용면적(㎡)"]) / 3.3 # 평당가 계산하여 새로운 컬럼 추가
df_apt1


# 사이드바 
def side_bar(df_apt1) :
  s_bar = st.sidebar
  s_bar.title('지역을 선택해주세요.')

  # 시/도 선택
  city_list = df_apt1['시군구'].apply(lambda x: x.split()[0]).unique()
  city_choice = s_bar.selectbox('시/도 선택', city_list)

  # 시/군/구 선택
  gu_list = df_apt1['시군구'][df_apt1['시군구'].str.contains(city_choice)].apply(lambda x: x.split()[1]).unique()
  gu_choice = s_bar.selectbox('시/군/구 선택', gu_list)

  # 읍/면/동 선택
  town_list = df_apt1['시군구'][df_apt1['시군구'].str.contains(city_choice) & df_apt1['시군구'].str.contains(gu_choice)].apply(lambda x: x.split()[2]).unique()
  town_choice = s_bar.selectbox('읍/면/동 선택', town_list)

  # 리 선택
  village_list = df_apt1['시군구'][df_apt1['시군구'].str.contains(city_choice) & df_apt1['시군구'].str.contains(gu_choice) & df['시군구'].str.contains(town_choice)].apply(lambda x: x.split()[3]).unique()
  village_choice = s_bar.selectbox('리 선택', village_list)

  # 선택된 지역의 데이터만 추출
  result = df_apt1[df_apt1['시군구'].str.contains(city_choice) & df_apt1['시군구'].str.contains(gu_choice) & df_apt1['시군구'].str.contains(town_choice) & df['시군구'].str.contains(village_choice)]

  # result 데이터프레임의 인덱스를 0->1부터 시작하도록 변경
  result.index = np.arange(1, len(result) + 1)

  return result


df_apt2 = pd.read_csv('Data/아파트_매매__실거래가_2월.csv')
df_apt2
