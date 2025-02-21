def jeongryeol(arr, N):
    c_txt = [0]*10
    for t in arr:
        if t == "ZRO":
            c_txt[0] += 1
        if t == "ONE":
            c_txt[1] += 1
        if t == "TWO":
            c_txt[2] += 1
        if t == "THR":
            c_txt[3] += 1
        if t == "FOR":
            c_txt[4] += 1
        if t == "FIV":
            c_txt[5] += 1
        if t == "SIX":
            c_txt[6] += 1
        if t == "SVN":
            c_txt[7] += 1
        if t == "EGT":
            c_txt[8] += 1
        if t == "NIN":
            c_txt[9] += 1
    for i in range(10):
        for j in range(c_txt[i]):
            if i == 0:
                print("ZRO",end=" ")
            if i == 1:
                print("ONE",end=" ")
            if i == 2:
                print("TWO",end=" ")
            if i == 3:
                print("THR",end=" ")
            if i == 4:
                print("FOR",end=" ")
            if i == 5:
                print("FIV",end=" ")
            if i == 6:
                print("SIX",end=" ")
            if i == 7:
                print("SVN",end=" ")
            if i == 8:
                print("EGT",end=" ")
            if i == 9:
                print("NIN",end=" ")
    print()
T = int(input())
for _ in range(T):
    tc, len = input().split()
    N = int(len)
    arr = list(input().split())
    print(f"{tc}")
    jeongryeol(arr, N)
