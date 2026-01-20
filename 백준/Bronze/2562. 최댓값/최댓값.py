arr = [int(input()) for _ in range(9)]
ans = max(arr)
print(ans)
print(arr.index(ans) + 1)