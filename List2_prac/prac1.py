N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
s = 0
for i in range(N):
    for j in range(M):
        if i == j or N-1-i == j:
            s += arr[i][j]
print(s)