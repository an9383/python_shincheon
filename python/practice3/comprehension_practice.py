


if __name__=="__main__":
    # data = ['a','b','c','d']
    # encode ={datum:num+1 for num, datum in enumerate(data)}
    # decode = {num+1: datum for num, datum in enumerate(data)}
    # print(encode)
    # print(decode)

    # # 순서쌍: 2중 for문 대표
    # obj = {}
    # for par in range(10):
    #     for son in range(5):
    #        obj[(par,son)] = par + son
    # print(obj)

    # obj = { (par,son): par+son for par in range(10) for son in range(5) if par%2==1 and son%2==0}
    # print(obj)

    # obj={}
    # for num in range(30):
    #     if num%2==0:
    #         obj[num]=0
    #     else:
    #         obj[num]=1
    # print(obj)

    #3항연산자
    # obj = {num:(0 if num%2==0 else 1) for num in range(30)}
    obj = {num:(0 if num%2==0 else 1) for num in range(30)}
    print(obj)
