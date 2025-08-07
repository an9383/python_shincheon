import pandas as pd

if __name__=="__main__":
    columns = ['이름','국어','영어','수학']
    score_df = pd.DataFrame(columns=columns,encodings='utf_8')
    john = ["John", 100, 95, 99]
    peter = ["Peter", 100, 95, 99]
    sue = ["Sue", 100, 95, 99]
    score_df.loc[0] = john
    score_df.loc[1] = peter
    score_df.loc[2] = sue
    # print(score_df.loc[2,'국어':'영어'])
    print(score_df.loc[[0,2], ['국어','수학']])
    score_df.to_csv('score.csv',encoding='utf_8')


