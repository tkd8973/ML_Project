import requests
import streamlit as st
import pandas as pd
import numpy as np


# 데이터 프레임 생성 main -> create_df
def create_df():
  # DF_URL
  df_URL = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EC%8B%9C%ED%97%98%EC%9E%A5%EC%86%8C_%EA%B0%80%EA%B3%B5%EC%B2%98%EB%A6%AC.csv"
  
  # df을 읽어 오면서 df언네임 삭제
  df = pd.read_csv(df_URL).iloc[:, 1:]

  # df인덱스 올림 // df출력시 0부터 인덱스가 출력되는걸 1올려 버림
  df.index += 1

  # df 반환 // main으로 다시 return 
  return df