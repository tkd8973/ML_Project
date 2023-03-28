import streamlit as st
from data import get_city_list

def main():
    with st.sidebar: sidebar()
    contents()

def sidebar() :
    title =  '지역을 선택해주세요.'
    st.title(title)
    label_city_list = '시/도 선택'
    st.selectbox(label_city_list, get_city_list())
    

def contents():
    pass

if __name__ == '__main__':
    main()
    st.write('hello :)')