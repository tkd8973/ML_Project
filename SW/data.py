import pandas as pd

def read_data():
    df_apt1 = pd.read_csv('https://raw.githubusercontent.com/jaiwon880/ML_Projiect/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8_%EB%A7%A4%EB%A7%A4__%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_20230321134120_1%EC%9B%94.csv')
    df_apt2 = pd.read_csv('https://raw.githubusercontent.com/jaiwon880/ML_Projiect/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8_%EB%A7%A4%EB%A7%A4__%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_20230321134120_2%EC%9B%94.csv')
    return df_apt1,df_apt2