arr1 = [1, 1, 2, 2, 2, 8]
arr2 = list(map(int, input().split()))
for i in range(6):
    ans = arr1[i] - arr2[i]
    print(ans, end=' ')