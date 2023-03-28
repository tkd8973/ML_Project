import streamlit as st
import pandas as pd
import numpy as np
import data
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

    
df = data.read_data()

def side_bar(df1) :
    s_bar = st.sidebar
    s_bar.title('지역을 선택해주세요.')

    city_list = df1['시군구'].apply(lambda x: x.split()[0]).unique()
    city_choice = s_bar.selectbox('시/도 선택', city_list)

    gu_list = df1['시군구'][df1['시군구'].str.contains(city_choice)].apply(lambda x: x.split()[1]).unique()
    gu_choice = s_bar.selectbox('시/군/구 선택', gu_list)

    town_list = df1['시군구'][df1['시군구'].str.contains(city_choice) & df1['시군구'].str.contains(gu_choice)].apply(lambda x: x.split()[2]).unique()
    town_choice = s_bar.selectbox('읍/면/동 선택', town_list)
    
    try :
        village_list = df1['시군구'][df1['시군구'].str.contains(city_choice) & df1['시군구'].str.contains(gu_choice) & df1['시군구'].str.contains(town_choice)].apply(lambda x: x.split()[3]).unique()
        village_choice = s_bar.selectbox('리 선택', village_list)
        result = df1[df1['시군구'].str.contains(city_choice) & df1['시군구'].str.contains(gu_choice) & df1['시군구'].str.contains(town_choice) & df1['시군구'].str.contains(village_choice)]
    except :
        result = df1[df1['시군구'].str.contains(city_choice) & df1['시군구'].str.contains(gu_choice) & df1['시군구'].str.contains(town_choice)]
        
    
    # 선택된 지역의 데이터만 추출
    
    # result 데이터프레임의 인덱스를 0->1부터 시작하도록 변경
    result.index = np.arange(1,len(result) + 1)

    return result

def Pre(datas):
    data=[]
    datas['거래금액(만원)']=(datas['거래금액(만원)'].str.replace(',','')).str.strip().astype(int)
    datas["평당가"] = (datas["거래금액(만원)"] / datas["전용면적(㎡)"]*0.3025) # 평당가 계산하여 새로운 컬럼 추가
    aa=datas['계약년월'].astype(str)
    bb=datas['계약일'].astype(str)
    datas['date'] = aa+bb
    datas['date'] = pd.to_datetime(datas['date'], format='%Y%m%d')
    datas['금리'] = datas.apply(lambda x: 3.25 if ((x['계약년월']== 202301) & (x['계약일'] < 13)) else 3.5, axis=1)
    datas.drop(['계약년월','계약일'],axis=1,inplace=True)
    datas.sort_values('date',ascending = True, inplace=True)
    datas.set_index('date',inplace=True)
    datas['거래유형'] = datas['거래유형'].apply(lambda x:0 if x=='중개거래' else 1)
    datas.dropna(inplace=True)
    datas['금리'] = 0.0
    datas.loc[((datas.index >= '2022-08-25')& (datas.index < '2022-10-12')), '금리'] = 2.5
    datas.loc[((datas.index >= '2022-10-12')& (datas.index < '2022-11-24')), '금리'] = 3.0
    datas.loc[((datas.index >= '2022-11-24')& (datas.index < '2023-01-13')), '금리'] = 3.25
    datas.loc[((datas.index >= '2023-01-13')), '금리'] = 3.5
    st.dataframe(datas)

    return datas

def knn(datas):
    train = datas.loc[datas.index < '2023-01-01']
    test = datas.loc[datas.index >= '2023-01-01']
    X_train = train.drop(['시군구','거래금액(만원)','평당가'],axis=1)
    y_train = train['거래금액(만원)']
    X_test = test.drop(['시군구','거래금액(만원)','평당가'],axis=1)
    y_test = test['거래금액(만원)']

    models = []
    for i in range(0,5):
        if i==0:
            continue
        model = KNeighborsRegressor(n_neighbors=i,weights='distance')
        model.fit(X_train,y_train)

        pred=model.predict(X_test)
        rmse = mean_squared_error(y_test,pred)**0.5
        
        models.append(rmse)

    st.write(models)

df = side_bar(df)
data = Pre(df)
print(data)
knn(data)