import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')



if __name__ == "__main__":
    tit_df = pd.read_csv("data/titanic_train.csv")
    tit_df.rename(columns= {'Sex':'Gender'}, inplace=True)
    tit_df.drop('Cabin', axis=1, inplace=True)
    tit_df['Age'].fillna(tit_df['Age'].mean(), inplace=True)
    tit_df['Embarked'].fillna('S', inplace=True)
    tit_df['Age'] = tit_df['Age'].astype(int)
    tit_df.sort_values('Age', ascending=False, inplace=True) # ascending=True
    # value_counts, unique, sort_values
    tit_df.info()
    print(tit_df["Age"])