
def func(x):
    mul = 4*x
    # print(avg)
    return mul

if __name__ == "__main__":
    # tf = 'd' in ['a','b','c','d','student']
    # print(tf)
    # for var in ['a','b','c']:
    #     print(var)
    # for var in "student":
    #     print(var)

    # obj = {'국어':100, '수학':85, '영어':95 }
    # obj['국어'] = 100
    # obj['영어'] = 95
    # obj['수학'] = 93
    # print(obj)
    # obj.keys()
    # print(obj.keys())
    # print(obj.values())
    # print(obj.items())

    # for key,value in obj.items():
    #     print(key,value)
    # for key in obj.keys():
    #     print(key)
    # for value in obj.values():
    #     print(value)
    # for _,value in obj.items():
    #     print(value)

    # arrs = []
    # numbers = range(10000)  #start(0), end, interval(1)
    # for num in numbers:
    #     if num%4 == 0:
    #         arrs.append(num)
    # print(arrs)

    # arrs = [num for num in range(1000) if num%4==0]
    # print(arrs)

    # list1 = ["국어","수학","영어","과학"]
    # list2 = [100,95,86,100]
    # items = list(zip(list1,list2))
    # print(items)    #list
    # obj = {}
    # for key,value in zip(list1,list2):
    #     obj[key] = value
    # print(obj)  #obj

    # obj = {key: value for key,value in zip(list1,list2)}    #comprehension
    # print(obj)

    # list1 = [1,2,2,2,3,3,3,4]
    # arrs = list(set(list1)) #중복제거
    # print(arrs)
    #
    # arrs = [100,89,99,73,60]
    # arrs = sorted(arrs)
    # arrs = arrs[::-1]
    # print(arrs)

    # list1 = ["국어","수학","영어","과학"]
    # list2 = [100,95,86,100]
    # arrs = list(zip(list1, list2))
    # print(arrs)
    # tuple1, tuple2 = zip(*arrs)
    # print(tuple1) #tuple로 풀림
    # print(tuple2) #tuple로 풀림

    # result = func(5)
    # print(result)

    results = list(map(func,[4,5,6,7]))
    print(results)





