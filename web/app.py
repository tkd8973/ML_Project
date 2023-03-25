import requests
import streamlit as st
import pandas as pd
import numpy as np


df_apt1 = pd.read_excel('https://github.com/jaiwon880/ML_Projiect/raw/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8(%EB%A7%A4%EB%A7%A4)_%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_1%EC%9B%94.xlsx')
df_apt1
df_apt2 = pd.read_excel('https://github.com/jaiwon880/ML_Projiect/raw/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8(%EB%A7%A4%EB%A7%A4)_%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_2%EC%9B%94.xlsx')
df_apt2
# # 사이드바 // 메인에서 df의 값을 받아온다. main -> create_df -> side_bar
# def side_bar(df) :
#   s_bar = st.sidebar
#   s_bar.title('지역을 선택해주세요.')

#   # area에 df에서 열 중에서 중복된 값들을 제외하고 리스트로 변환
#   area = df['시군구'].drop_duplicates().tolist()

#   # selectbox에 위 area의 인덱스 10인 "서울특별시"를 초기 값으로 잡고 choice라는 변수에 셀렉트박스의 선택된 값을 저장
#   choice = s_bar.selectbox('지역 선택(재검색시 상세 검색을 지워 주세요)', area, index = 10)

#   # 위 area 리스트의 크기 만큼 반복 그냥 if문을 area의 리스트 크기만큼 작성
#   for i in range(len(area)):
#     # 초이스 셀렉트바에서 선택한 값이 area의 인덱스 값과 일치한다면
#     if choice == area[i]: 
#       result = df[df['시군구'] == area[i]] # result에 지사명이 지역을 선택한 값들의 데이터들은 저장
#     else : pass # 아닌 경우 패스
   
#   # 검색바 생성 후 입력된 값을 변수 search에 저장 
#   search = s_bar.text_input('상세 검색 (시, 교명등의 키워드를 입력 :smile:)')

#   # 지역선택한 값 안에서 시험장소를 검색(입력, 위의 search)한 값과 일치하는 값을 담는다.
#   result = df[(df['시군구'] == choice) & (df['시험장소'].str.contains(search))]

#   # result 데이터프레임의 인덱스를 0->1부터 시작하도록 변경 // 지역 변경시 마다 각 행의 고유 인덱스 번호로 출력이 되는걸 1번 부터로 출력하게함
#   result.index = np.arange(1, len(result) + 1) 

#   return result # 데이터프레임과 지역선택의 값을 return // main으로 다시 return