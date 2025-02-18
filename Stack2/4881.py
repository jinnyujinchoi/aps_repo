def f(i, N):        # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global min_v
    global cnt
    cnt += 1

    if i == N:
        s = 0
        for j in range(N):  # j 행에서 고른 열 p[j]
            s += arr[j][p[j]]
        if min_v > s:
            min_v = s
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]     # 자리 교환
            f(i+1, N)       # i+1 자리 결정
            p[i], p[j] = p[j], p[i]     # 원상 복구


N = int(input())    # 배열의 크기 N*N
arr = [list(map(int, input().split())) for _ in range(N)]

p = [ i for i in range(N)]  # P[i] : i에서 고른 열 번호
min_v = 10000
f(0, N)
print(min_v)