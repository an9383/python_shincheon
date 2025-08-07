
def average(kor,math,eng):
    avg =(kor+math+eng)/3   # average의 avg로 받아들임.
    return avg

print("map_practice_up")

if __name__ == "__main__":  # Script 파일이름  == 실행 파일이름
    # avg = average(89,94,100) # if의 avg로 받아들임.
    # print(avg)

    # stud_kors = [89, 94, 100]
    # stud_maths = [94, 87, 99]
    # stud_engs = [100, 84, 93]
    # avgs = map(average, stud_kors, stud_maths, stud_engs)
    # print(list(avgs))

    stud_kors = [89, 94, 100]
    stud_maths = [94,87, 99]
    stud_engs = [100, 84, 93]

    for avg in map(average,stud_kors,stud_maths, stud_engs):
        print(avg)

    print("map_practice_down")

