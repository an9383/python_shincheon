import pandas as pd


if __name__=="__main__":
    score = pd.DataFrame(columns=[ "국어", "영어", '수학'])
    score.loc[0] = [100, 98, 83]
    score.loc[1] = [83, 78, 90]
    score.loc[2] = [89, 91, 75]

    score['평균'] = (score['국어']+score['영어']+score['수학'])/3
    # lang_mean = score['국어'].mean()
    result = score.mean(axis=1)     # 1번이 x축 평균, 0번은 y축 평균
    print(score)
    # print(lang_mean)
    print(result)