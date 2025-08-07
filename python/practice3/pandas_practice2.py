import pandas as pd

customer = pd.DataFrame(columns=['cust_id',"cust_name","cust_address",'cust_phone'])
book = pd.DataFrame(columns=['book_id',"book_name","book_price"])
order = pd.DataFrame(columns=['order_id','cust_id','book_id',"cust_date"])

if __name__=="__main__":
    customer.loc[0] = [1, 'John', "Seoul", "010-1111-1111"]
    customer.loc[1] = [2, 'Peter', "Pusan", "010-2222-2222"]
    customer.loc[2] = [3, 'Bob', "Inchon", "010-3333-3333"]
    customer.loc[3] = [4, 'John', "Daegu", "010-4444-4444"]

    # customer.loc[1,'cust_phone'] = "010-5555-5555"
    # print(customer)

    book.loc[0] = [1, 'Python', 25000]
    book.loc[1] = [2, 'Java', 40000]
    book.loc[2] = [3, 'JavaScript', 35000]
    book.loc[3] = [4, 'React', 3000]

    order.loc[0] = [1,2,3,1]
    order.loc[1] = [2,4,1,2]
    order.loc[2] = [3,2,1,3]
    order.loc[3] = [4,1,4,4]

    # print(customer)
    # print(book)
    # print(order)

    # cust_ord_merged_df = pd.merge(order, customer, on='cust_id', how='inner')
    # book_ord_merged_df = pd.merge(order, book, on='book_id', how='inner')
    total_merged_df = pd.merge(pd.merge(customer,order, on="cust_id", how='inner'),
                               book,
                               on = "book_id",
                               how='inner')[['cust_name','book_name','book_price']]
    # print(cust_ord_merged_df)
    # print(book_ord_merged_df)
    # print(book_ord_merged_df[['book_name','book_price']])

    # peter_info = total_merged_df[total_merged_df['cust_name']=='Peter']
    # peter_max_order_price_info = peter_info[peter_info['book_price'] == peter_info['book_price'].max()]
    # print(peter_max_order_price_info)

    # price = total_merged_df['book_price'].max()
    # print(price)









