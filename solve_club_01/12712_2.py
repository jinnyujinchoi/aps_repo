def solve(arr, N):
    hs = 0
    for i in range(N):
        for j in range(N):
            cs = arr[i][j]
            for di, dj in [[0, 1], [1, 0], [0, -1],[-1, 0]]:
                for k in range(1, M):
                    ni, nj = i+di*k, j+dj*k
                    if 0 <= ni < N and 0 <= nj < N:
                        cs += arr[ni][nj]
            if hs < cs:
                hs = cs
            xs = arr[i][j]
            for di, dj in [[1, 1], [-1, -1], [1, -1], [-1, 1]]:
                for k in range(1, M):
                    ni, nj = i+di*k, j+dj*k
                    if 0 <= ni < N and 0 <= nj < N:
                        xs += arr[ni][nj]
            if hs < xs:
                hs = xs
    return hs

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {solve(fly, N)}")