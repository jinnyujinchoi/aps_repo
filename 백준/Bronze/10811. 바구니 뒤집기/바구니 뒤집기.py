N, M = map(int, input().split())
arr = [i+1 for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    t = j-i+1
    # 차이가 0이면
    if t == 1:
        continue
    else:
        for x in range(t//2):
            arr[i-1+x], arr[j-1-x] = arr[j-1+-x], arr[i-1+x]

print(*arr)