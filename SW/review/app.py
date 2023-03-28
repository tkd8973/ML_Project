import streamlit as st
import glob
def main():
    with st.sidebar: sidebar()
    contents()

def sidebar() :
    title =  '지역을 선택해주세요.'
    st.title(title)
    st.write(glob.glob('static'))

def contents():
    pass

if __name__ == '__main__':
    main()
    st.write('hello :)')