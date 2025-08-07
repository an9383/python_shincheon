def GCD(first,second):
    while True:
        r = first % second
        first = second
        second = r
        if r == 0:
            return first

if __name__=="__main__":
    # pass
    gcd = GCD(72,48)
    print(gcd)