def f(i, j, s):
    global min_v
    if i==N-1 and j==N-1:
        if min_v > s + arr[i][j]:
            min_v = s + arr[i][j]
    else:
        if i+1 < N:
            f(i+1, j, s+arr[i][j])
        if j+1 < N:
            f(i, j+1, s+arr[i][j])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_v = 1000
    f(0, 0, 0)

    print(f"#{tc} {min_v}")