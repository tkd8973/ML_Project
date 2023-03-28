import requests
import streamlit as st
import pandas as pd
import numpy as np
import os
# import xgboost as xgb
# xgb_model = xgb.XGBRegressor()


st.write(
    """
    ## 🏢 아파트 실거래가 예측
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



tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(["Linear Regression", "KNN", "Decision Tree", "Random Forest", "XGBoost", "LightGBM"])

with tab0:
    tab0.subheader("Linear Regression")
    st.write()
    '''
    ⬆️위의 탭에 있는 메뉴를 클릭해 선택하신 항목을 볼 수 있습니다!⬆️
    ---
    '''

    
    col1,col2 = st.columns([1,1])
    # 공간을 1:1 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성

    with col1 :
        # column 1 에 담을 내용
        st.info('자치구별 동물 병원수 입니다.', icon="ℹ️")
        
        st.info('자치구별 동물 미용업체수 입니다.', icon="ℹ️")

        st.info('자치구별 반려동물 보유비율입니다.', icon="ℹ️")



    with col2 :
        # column 2 에 담을 내용
        st.info('자치구별 동물 위탁시설 수 입니다.', icon="ℹ️")
        
        st.info('자치구별 공원 시설 수 입니다.', icon="ℹ️")

        st.info('자치구별 종합 순위 입니다.', icon="ℹ️")




with tab1:
    tab1.subheader("📈KNN")
    tab1.write()
    
    option = st.selectbox(
    '원하는 차트유형을 골라주세요',
    ('Bar', 'Pie', 'Heatmap'))
    if option == 'Bar':
        option = st.selectbox(
        '원하는 차트를 골라주세요',
        ('성별에 따른 상품 구매량', '평일/주말에 따른 상품 구매량', '나이에 따른 상품 구매량'))
        if option == '성별에 따른 상품 구매량':
            st.write("성별에 따른 상품구매량")
            hist_plot(datas,'sex','Tag')

        elif option == '평일/주말에 따른 상품 구매량':
            st.write("평일/주말에 따른 상품 구매량")
            hist_plot(datas,'weekday','Tag')

        elif option == '나이에 따른 상품 구매량':
            st.write("평일/주말에 따른 상품 구매량")
            hist_plot(datas,'age','Tag')

    elif option == 'Pie':
        st.write("년도별 성별에 따른 상품 구매량")
        pie()    
    elif option == 'Heatmap':
        st.write("히트맵 인덱스가 날아가네요 자세한건 Colab에서")
         
with tab2:
    tab2.subheader("Decision Tree")
    datas.head()
    tab2.write()

    
with tab3:
    tab3.subheader("Random Forest")
    tab3.write("")
    st.write("")

with tab4:
    tab4.subheader("XGBoost")
    tab4.write("")


with tab5:
    tab5.subheader("LightGBM")
    tab5.write("")



 '''
    ### Team
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
    * 아파트 실거래가 2022년 3월 ~ 2023년 2월까지의 데이터 입니다.
    > [데이터 다운로드]()
    * 데이터출처 : Dacon
    ---
    '''