N, M = map(int, input().split())
arr = list(i+1 for i in range(N))
for _ in range(M):
    a, b = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
print(*arr)