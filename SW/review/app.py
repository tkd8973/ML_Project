import streamlit as st
from data import get_city_list, get_gu_list

def main():
    with st.sidebar: sidebar()
    contents()

def sidebar() :
    title =  '지역을 선택해주세요.'
    st.title(title)
    label_city_list = '시/도 선택'
    city_choice = st.selectbox(label_city_list, get_city_list())
    st.selectbox(label_city_list, get_gu_list(city_choice))


def contents():
    pass

if __name__ == '__main__':
    main()
    st.write('hello :)')