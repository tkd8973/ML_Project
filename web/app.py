import requests
import streamlit as st
import pandas as pd
import numpy as np

import os

# url = 'https://github.com/jaiwon880/ML_Projiect/raw/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8(%EB%A7%A4%EB%A7%A4)_%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_1%EC%9B%94.xlsx'
# file_name = 'apt_data.xlsx'

# response = requests.get(url)

st.write(
    """
    ## 어려운 부동산 ^_^...
    ---
    """
)

# df = pd.read_csv(url,engine='openpyxl')

df_apt1 = pd.read_excel('https://github.com/jaiwon880/ML_Projiect/raw/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8(%EB%A7%A4%EB%A7%A4)_%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_1%EC%9B%94.xlsx')
df_apt1
# df_apt2 = pd.read_excel('https://github.com/jaiwon880/ML_Projiect/blob/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8(%EB%A7%A4%EB%A7%A4)_%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_2%EC%9B%94.xlsx')
# df_apt2

st.sidebar.title('선택해라')
selected_region = st.sidebar.selectbox("행정구역 선택해라", 'ㅎㅇ'
)




# df_apt1 = pd.read_excel('https://github.com/jaiwon880/ML_Projiect/raw/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8(%EB%A7%A4%EB%A7%A4)_%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_1%EC%9B%94.xlsx')
# df_apt1
# df_apt2 = pd.read_excel('https://github.com/jaiwon880/ML_Projiect/raw/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8(%EB%A7%A4%EB%A7%A4)_%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_2%EC%9B%94.xlsx')
# df_apt2


# # 사이드바 
# def side_bar(df) :
#   s_bar = st.sidebar
#   s_bar.title('지역을 선택해주세요.')

  #   시/도 선택
  #   city_list = df['시군구'].apply(lambda x: x.split()[0]).unique()
  #   city_choice = s_bar.selectbox('시/도 선택', city_list)

  #   # 시/군/구 선택
  #   gu_list = df['시군구'][df['시군구'].str.contains(city_choice)].apply(lambda x: x.split()[1]).unique()
  #   gu_choice = s_bar.selectbox('시/군/구 선택', gu_list)

  #   # 읍/면/동 선택
  #   town_list = df['시군구'][df['시군구'].str.contains(city_choice) & df['시군구'].str.contains(gu_choice)].apply(lambda x: x.split()[2]).unique()
  #   town_choice = s_bar.selectbox('읍/면/동 선택', town_list)

  #   # 리 선택
  #   village_list = df['시군구'][df['시군구'].str.contains(city_choice) & df['시군구'].str.contains(gu_choice) & df['시군구'].str.contains(town_choice)].apply(lambda x: x.split()[3]).unique()
  #   village_choice = s_bar.selectbox('리 선택', village_list)

  #   # 선택된 지역의 데이터만 추출
  #   result = df[df['시군구'].str.contains(city_choice) & df['시군구'].str.contains(gu_choice) & df['시군구'].str.contains(town_choice) & df['시군구'].str.contains(village_choice)]

  #   # result 데이터프레임의 인덱스를 0->1부터 시작하도록 변경
  #   result.index = np.arange(1, len(result) + 1)
  # return result