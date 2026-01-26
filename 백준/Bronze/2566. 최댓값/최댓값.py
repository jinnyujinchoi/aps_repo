arr = [list(map(int, input().split())) for _ in range(9)]
maxVal = 0
ans_i, ans_j = 1, 1
for i in range(9):
    for j in range(9):
        if arr[i][j] > maxVal:
            maxVal = arr[i][j]
            ans_i, ans_j = i+1, j+1
print(maxVal)
print(ans_i, ans_j)