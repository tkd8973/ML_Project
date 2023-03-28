import pandas as pd

def read_data():
    df_9 = pd.read_csv('https://github.com/tkd8973/ML_Project/raw/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8_%EB%A7%A4%EB%A7%A4__%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_20230321133950_9%EC%9B%94.csv')
    df_10 = pd.read_csv('https://github.com/tkd8973/ML_Project/raw/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8_%EB%A7%A4%EB%A7%A4__%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_20230321134004_10%EC%9B%94.csv')
    df_11 = pd.read_csv('https://github.com/tkd8973/ML_Project/raw/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8_%EB%A7%A4%EB%A7%A4__%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_20230321134031_11%EC%9B%94.csv')
    df_12 = pd.read_csv('https://github.com/tkd8973/ML_Project/raw/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8_%EB%A7%A4%EB%A7%A4__%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_20230321134043_12%EC%9B%94.csv')
    df_1 = pd.read_csv('https://github.com/jaiwon880/ML_Projiect/raw/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8_%EB%A7%A4%EB%A7%A4__%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_20230321134107_1%EC%9B%94.csv')
    df_2 = pd.read_csv('https://raw.githubusercontent.com/jaiwon880/ML_Projiect/main/Data/%EC%95%84%ED%8C%8C%ED%8A%B8_%EB%A7%A4%EB%A7%A4__%EC%8B%A4%EA%B1%B0%EB%9E%98%EA%B0%80_20230321134120_2%EC%9B%94.csv')
    
    df = pd.concat([df_9,df_10,df_11,df_12,df_1,df_2])
    return df