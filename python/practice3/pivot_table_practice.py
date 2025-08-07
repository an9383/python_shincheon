from pandas_practice2 import customer, book, order
import pandas as pd


customer.loc[0] = [1, 'John', "Seoul", "010-1111-1111"]
customer.loc[1] = [2, 'Peter', "Pusan", "010-2222-2222"]
customer.loc[2] = [3, 'Bob', "Inchon", "010-3333-3333"]
customer.loc[3] = [4, 'Sue', "Daegu", "010-4444-4444"]

customer.loc[1, "cust_phone"] = "010-5555-5555"
# print(customer)

book.loc[0] = [1, 'Python', 25000]
book.loc[1] = [2, 'Java', 40000]
book.loc[2] = [3, 'JavaScript', 35000]
book.loc[3] = [4, 'React', 30000]

order.loc[0] = [1, 2, 3, 1]
order.loc[1] = [2, 4, 1, 2]
order.loc[2] = [3, 2, 1, 3]
order.loc[3] = [4, 1, 4, 4]

total_merged_df = pd.merge(
        pd.merge(customer, order, on="cust_id", how='inner'),
        book,
        on="book_id",
        how='inner'
    )[['cust_name', "book_name", "book_price"]]




if __name__ == "__main__":

    # df = total_merged_df.pivot_table(index='cust_name', values='book_price',aggfunc=['mean', 'max', 'min'])
    # print(df)
    df = total_merged_df.pivot_table(
        index='cust_name',
        columns='book_name',
        values='book_price',
        fill_value=0
    )
    print(df)