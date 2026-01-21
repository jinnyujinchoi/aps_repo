arr1 = [int(input()) for _ in range(28)]
arr2 = [i+1 for i in range(30)]
ans = set(arr2) - set(arr1)
print(min(ans))
print(max(ans))