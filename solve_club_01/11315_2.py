def concave(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for di, dj in [[0,1], [1,0], [1,1], [-1,1]]:
                    cnt = 1
                    for k in range(1, 5):
                        ni, nj = i+di*k, j+dj*k
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 'o':
                            cnt += 1
                    if cnt == 5:
                        return "YES"
    return "NO"


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stone = [list(input()) for _ in range(N)]
    print(f"#{tc} {concave(stone, N)}")