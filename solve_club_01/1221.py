def jeongryeol(arr, N):     # 정렬해주는 함수
    c_txt = [0]*10      # 위치 인덱스 기반으로 각각의 개수 세주는 리스트
    for t in arr:       # input받은 리스트를 돌면서~
        if t == "ZRO":      # ZRO라는 문자열이면
            c_txt[0] += 1   # 0 인덱스에 개수 하나 추가
        if t == "ONE":      # 쭉 동일
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
    for i in range(10):             # 0~9까지 돌아주면서
        for j in range(c_txt[i]):   # ex)0의 개수만큼 반복하며 출력!
            if i == 0:              # 인덱스 0 / 즉 ZRO면
                print("ZRO",end=" ")    # ZRO 개수만큼 반복 출력
            if i == 1:
                print("ONE",end=" ")    # end=" " 는 출력 사이 공백 주기
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
    print() # 0에 대한 반복이 끝나면 enter
T = int(input())
for _ in range(T):
    tc, len = input().split()
    N = int(len)
    arr = list(input().split())
    print(f"{tc}")      # 테스트 케이스 번호 출력하고
    jeongryeol(arr, N)  # 함수 호출하고
