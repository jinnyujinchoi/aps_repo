N, K = map(int, input().split())
arr = []

for i in range(1, int(N ** 0.5)+1):
    if N % i == 0:
        arr.append(i)
        if i != N // i:
            arr.append(N // i)
arr.sort()
if len(arr) < K:
    ans = 0
else:
    ans = arr[K-1]
print(ans)