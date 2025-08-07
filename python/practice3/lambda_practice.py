

if __name__=="__main__":
    # stud_kors = [89, 94, 100]
    # stud_maths = [94, 87, 99]
    # stud_engs = [100, 84, 93]
    #
    # avgs = map(lambda kor,math,eng: (kor+math+eng)/3,
    #            stud_kors,stud_maths,stud_engs)
    # print(list(avgs))

    lamb = lambda kor,math,eng: (kor+math+eng)/3
    avg = lamb(90,89,83)
    print(avg)