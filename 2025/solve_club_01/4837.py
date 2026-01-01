A = [1,2,3,4,5,6,7,8,9,10,11,12]
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0 # 부분집합 개수 초기화
    for i in range(1<<12):
        s_sub = 0 # 합 초기화
        sub_lst = [] # 조건 충족 리스트 초기화
        for j in range(12):
            if i&(1<<j):
                sub_lst.append(A[j])
                s_sub += A[j]
        # 합이 K, 개수가 N이면
        if s_sub == K and len(sub_lst) == N:
            cnt += 1
    print(f"#{tc} {cnt}")

