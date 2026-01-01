def solve(arr, N, M):
    hs = 0
    for i in range(N):
        for j in range(M):
            s = arr[i][j]
            c = arr[i][j]
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for k in range(1, c+1):
                    ni, nj = i+di*k, j+dj*k
                    if 0<=ni<N and 0<=nj<M:
                        s += arr[ni][nj]
            if hs < s:
                hs = s
    return hs

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stage = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {solve(stage, N, M)}")