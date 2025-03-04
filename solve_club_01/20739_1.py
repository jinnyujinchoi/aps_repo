def solve(arr):
    max_l = 0
    for i in range(N):
        l = 0
        for j in range(M):
            if arr[i][j] == 1:
                l += 1
                if max_l < l:
                    max_l = l
            else:
                l = 0

    for j in range(M):
        l = 0
        for i in range(N):
            if arr[i][j] == 1:
                l += 1
                if max_l < l:
                    max_l = l
            else:
                l = 0

    if max_l == 1:
        return 0
    else:
        return max_l


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {solve(land)}")