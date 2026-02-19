N = int(input())
arr = list(map(int, input().split()))
arr2 = []
M = max(arr)
for x in arr:
    x = x/M*100
    arr2.append(x)
ans = sum(arr2)/N
print(ans)