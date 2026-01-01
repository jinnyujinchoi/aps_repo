def solve(arr, N):
    s = 0
    p = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                s += 1
            elif arr[i][j] == 2:
                for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                    for k in range(1, N):
                        ni, nj = i+di*k, j+dj*k
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
                            p += 1
                        else:
                            break
    return s-p

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {solve(area, N)}")