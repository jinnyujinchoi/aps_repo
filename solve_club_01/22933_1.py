def solve(arr, N):
    max_s = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            s = 0
            for ni in range(i, N):
                for nj in range(j, N):
                    if 0<=ni<N and 0<=nj<N:
                        if arr[i][j] == arr[ni][nj]:
                            s = (ni-i+1)*(nj-j+1)
                            if max_s < s:
                                max_s = s
                                cnt = 1
                            elif max_s == s:
                                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{tc} {solve(arr, N)}")
