import streamlit as st
import glob
import os

def main():
    with st.sidebar: sidebar()
    contents()

def sidebar() :
    title =  '지역을 선택해주세요.'
    st.title(title)
    print(__file__)
    print(os.path.realpath(__file__))
    print(os.path.abspath(__file__))
    st.write(glob.glob('static/*.csv'))

def contents():
    pass

if __name__ == '__main__':
    main()
    st.write('hello :)')