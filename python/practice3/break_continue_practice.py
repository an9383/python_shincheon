from contextlib import nullcontext

def identify(num):
    if num%2 == 0:
        print("even")
        return
    if num % 2 == 1:
        print("odd")
        return


if __name__=="__main__":
    # # p,q = 96,89
    # p,q= 86, 48
    # while True:
    #     r = p%q
    #     p=q
    #     q=r
    #     if r == 0:
    #         print(p)
    #         break

    # for num in range(30):
    #     if num % 2 == 0:
    #         continue
    #     print(num)

    result = identify(89)
    print(result)
