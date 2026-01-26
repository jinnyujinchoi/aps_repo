arr = [list(input()) for _ in range(5)]
ans = []
maxLen = max(len(row) for row in arr)
for j in range(maxLen):
    for i in range(5):
        if j < len(arr[i]):
            ans.append(arr[i][j])
print(''.join(ans))