import requests
import streamlit as st
import pandas as pd
import numpy as np
import os
# import xgboost as xgb
# xgb_model = xgb.XGBRegressor()


st.write(
    """
    ## 🏙️ 아파트 실거래가 예측
    ---
    """
)

# st.sidebar.title('선택해라')
# selected_region = st.sidebar.selectbox("행정구역 선택해라", city_list
# )


df_apt1 = pd.read_csv('Data/아파트_매매__실거래가_20230321134107_1월.csv')
df_apt2 = pd.read_csv('Data/아파트_매매__실거래가_20230321134120_2월.csv')

df_apt1["거래금액(만원)"] = df_apt1["거래금액(만원)"].str.replace(",", "").astype(int) # 거래금액 컬럼의 쉼표를 제거하고 정수형으로 변환
df_apt1["평단가"] = (df_apt1["거래금액(만원)"] / df_apt1["전용면적(㎡)"]) / 3.3 # 평당가 계산하여 새로운 컬럼 추가



# 사이드바 // 메인에서 df의 값을 받아온다. main -> create_df -> side_bar
def side_bar(df1,df2) :
    s_bar = st.sidebar
    s_bar.title('지역을 선택해주세요.')

    # area에 df에서 열 중에서 중복된 값들을 제외하고 리스트로 변환
    # 시/도 선택

    city_list = df1['시군구'].apply(lambda x: x.split()[0]).unique()
    city_choice = s_bar.selectbox('시/도 선택', city_list)

    # 시/군/구 선택
    gu_list = df1['시군구'][df1['시군구'].str.contains(city_choice)].apply(lambda x: x.split()[1]).unique()
    gu_choice = s_bar.selectbox('시/군/구 선택', gu_list)

    # 읍/면/동 선택
    town_list = df1['시군구'][df1['시군구'].str.contains(city_choice) & df1['시군구'].str.contains(gu_choice)].apply(lambda x: x.split()[2]).unique()
    town_choice = s_bar.selectbox('읍/면/동 선택', town_list)
    
    # 리 선택
    try :
        village_list = df1['시군구'][df1['시군구'].str.contains(city_choice) & df1['시군구'].str.contains(gu_choice) & df1['시군구'].str.contains(town_choice)].apply(lambda x: x.split()[3]).unique()
        village_choice = s_bar.selectbox('리 선택', village_list)
        Jan_result = df1[df1['시군구'].str.contains(city_choice) & df1['시군구'].str.contains(gu_choice) & df1['시군구'].str.contains(town_choice) & df1['시군구'].str.contains(village_choice)]
        Feb_result = df2[df2['시군구'].str.contains(city_choice) & df2['시군구'].str.contains(gu_choice) & df2['시군구'].str.contains(town_choice) & df2['시군구'].str.contains(village_choice)]
    except :
        Jan_result = df1[df1['시군구'].str.contains(city_choice) & df1['시군구'].str.contains(gu_choice) & df1['시군구'].str.contains(town_choice)]
        Feb_result = df2[df2['시군구'].str.contains(city_choice) & df2['시군구'].str.contains(gu_choice) & df2['시군구'].str.contains(town_choice)]

    
    # 선택된 지역의 데이터만 추출
    
    # result 데이터프레임의 인덱스를 0->1부터 시작하도록 변경
    Jan_result.index = np.arange(1,len(Jan_result) + 1)
    Feb_result.index = np.arange(1,len(Feb_result) + 1)
    result = pd.concat([Jan_result,Feb_result])
    st.dataframe(result)

    return Jan_result, Feb_result

df1,df2 = side_bar(df_apt1,df_apt2)


# 서상원

[조성훈](https://www.notion.so/4242b17b112e4d0dbb8c471cec922009)

[곽희범](https://www.notion.so/5efb83ab746146ddaf5269ffc7f26c44)

[이영미](https://www.notion.so/a42f95e4f64e4f74a5d5a4e75e006ba6)

[한재원](https://www.notion.so/4145284160484740904e35a70f4f4472)

[박상원](https://www.notion.so/66fdc324aa2742e79e6e6d4e62339875)

[이영재](https://www.notion.so/4271ee70757c40988d86876a93369a46)

[최용재](https://www.notion.so/429ad829acb447d3a084b6e9c4abab9d)