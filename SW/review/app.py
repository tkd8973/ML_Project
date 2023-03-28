import streamlit as st
from data import read_data

def main():
    with st.sidebar: sidebar()
    contents()

def sidebar() :
    title =  '지역을 선택해주세요.'
    st.title(title)
      
    st.write(read_data())

def contents():
    pass

if __name__ == '__main__':
    main()
    st.write('hello :)')