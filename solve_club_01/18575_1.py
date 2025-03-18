def score(arr, N):
    hs = 0              # 하이스코어 초기화
    ls = 39*9           # 로우스코어 초기화
    for i in range(N):
        for j in range(N):
            s = arr[i][j]       # 현재 합 초기화(본인 포함)
            for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                for k in range(1, N):
                    ni, nj = i+di*k, j+dj*k
                    if 0<=ni<N and 0<=nj<N:
                        s += arr[ni][nj]
            if hs < s:
                hs = s
            if ls > s:
                ls = s
    return hs - ls

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stage = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {score(stage, N)}")