import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import Decisor
import xgboost as xgb
import lightgbm as lgbionTreeRegressor
from xgboost import XGBRegress
from data import get_city_list, get_gu_list, get_town_list, get_village_list
from service import get_filtered_data, handle_preprocessing

def main():
    with st.sidebar: sidebar()
    contents()

def sidebar() :
    title =  '지역을 선택해주세요.'
    st.title(title)
    label_city_list = '시/도 선택'
    label_gu_list = '시/군/구 선택'
    label_town_list = '읍/면/동 선택'
    city_choice = st.selectbox(label_city_list, get_city_list(),
    key='city')
    gu_choice = st.selectbox(label_gu_list, get_gu_list(city_choice),
    key='gu')
    town_choice = st.selectbox(label_town_list, get_town_list(city_choice, gu_choice),
    key='town')
    vl = get_village_list(city_choice, gu_choice, town_choice)
    if vl:
        village_choice = st.selectbox(label_town_list, vl, key='village')
    else:
        st.session_state['village'] = ''


def contents():
    # st.write(get_filtered_data())
    # st.write(handle_preprocessing())
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Linear Regressor", 'KNN', "Decision Tree", 'Random Forest', "XGBoost", "LightGBM"])
    with tab1: lr() 
    with tab2: knn()
    with tab3: dct()
    with tab4: rdf()
    with tab5: xgb()
    with tab6: lgbm()


# lr 모델
def lr():
    datas = handle_preprocessing()
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
        model = LinearRegression(n_jobs=-1)
        model.fit(X_train,y_train)

        pred= model.predict(X_test)
        rmse = mean_squared_error(y_test,pred)**0.5
        
        models.append(rmse)
    st.write('모델의 RMSE 값',models)


# knn 모델
def knn():
    datas = handle_preprocessing()
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


# 랜덤포레스트 모델
def rdf():
    datas = handle_preprocessing()
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
        model = RandomForestRegressor(n_estimators=150,max_depth=4)
        model.fit(X_train,y_train)

        pred=model.predict(X_test)
        rmse = mean_squared_error(y_test,pred)**0.5
        
        models.append(rmse)

    st.write(models)

# 결정트리 모델
def dct():
    datas = handle_preprocessing()
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
        model = DecisionTreeRegressor(random_state=i)
        model.fit(X_train,y_train)

        pred=model.predict(X_test)
        rmse = mean_squared_error(y_test,pred)**0.5
        
        models.append(rmse)

    st.write(models)

# XGBoost 모델
def xgb():
    datas = handle_preprocessing()
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
        model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=100)
        model.fit(X_train,y_train)

        pred=model.predict(X_test)
        rmse = mean_squared_error(y_test,pred)**0.5
        models.append(rmse)

    st.write(models)

# LGBM 모델
def lgbm():
    datas = handle_preprocessing()
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
        model = lgb.LGBMRegressor(num_leaves=16, max_depth=4, learning_rate=0.1)
        model.fit(X_train,y_train)

        pred=model.predict(X_test)
        rmse = mean_squared_error(y_test,pred)**0.5
        models.append(rmse)

    st.write(models)


if __name__ == '__main__':
    main()