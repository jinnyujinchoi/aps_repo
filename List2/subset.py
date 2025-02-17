a = [2, 3, 7, 9]
bit = [0]*4 # bit는 해당 자리에 값이 있는지, 없는지 확인함!
for i in range(2): # bit의 값은 0, 1
    bit[0] = i # 0번 원소
    for j in range(2):
        bit[1] = j # 1번 원소
        for k in range(2):
            bit[2] = k # 2번 원소
            for l in range(2):
                bit[3] = l # 3번 원소
                # 부분집합 출력
                for b in range(4):
                    if bit[b]: # bit[b]가 1이면,
                        print(a[b], end =' ')
                print()