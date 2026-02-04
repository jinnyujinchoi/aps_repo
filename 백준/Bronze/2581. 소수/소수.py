M = int(input())
N = int(input())
arr = []
for x in range(M, N+1):
    if x < 2:
        continue

    for i in range(2, x):
        if x % i == 0:
            break
    else:
        arr.append(x)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))