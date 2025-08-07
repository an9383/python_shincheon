import pandas as pd
import pickle









if __name__ == "__main__":
    # csv 파일 읽기
    # df = pd.read_csv("data/ratings.dat",
    #                  sep='::',
    #                  names=['user_id', "movie_id", "rating", "date"])
    # df = df.loc[:1000, :]

    # csv 파일 저장하기
    # df.to_csv('data/ratings.csv')
    # exit()
    # 피보팅
    df = pd.read_csv("data/ratings.csv")

    df.drop('user_id', axis=1, inplace=True)


    # print(df.shape)
    # print(df.info())
    # print(df.describe())
    # print(df.keys())

    # rating_pivot_table = df.pivot_table(
    #     index='user_id',
    #     columns='movie_id',
    #     values='rating',
    #     fill_value=df['rating'].mean()
    # )
    # print(rating_pivot_table)
    # with open('data/rating_pivot_table.pkl', 'wb') as pkl:
    #     pickle.dump(rating_pivot_table, pkl)

    # with open('data/rating_pivot_table.pkl', 'rb') as file:
    #     df = pickle.load(file)
    # print(df)
