board = [[0]*100 for _ in range(100)]
ans = 0

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    # 순회
    for i in range(x, 10+x):
        for j in range(y, 10+y):
            if board[i][j] == 1: # 이미 칠한 부분이면 skip
                continue
            if board[i][j] == 0:
                board[i][j] = 1
                ans += 1
# 순회 끝
print(ans)