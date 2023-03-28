import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor

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
    tab1, tab2 = st.tabs(['KNN 모델', '랜덤 포레스트 모델'])
    with tab1: knn()
    with tab2: RdForest()

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

def RdForest():
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

if __name__ == '__main__':
    main()