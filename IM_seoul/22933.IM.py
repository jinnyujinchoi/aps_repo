T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    COUNTS = [0] * (N * N + 1)
    for i in range(N):
        for j in range(N):
            COUNTS[arr[i][j]] += 1
    print(f"#{tc} {COUNTS}")