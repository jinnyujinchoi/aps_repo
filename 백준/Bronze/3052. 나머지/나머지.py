arr1 = [int(input()) for _ in range(10)]
arr2 = [i%42 for i in arr1]
ans = len(set(arr2))
print(ans)