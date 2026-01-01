# 4*4 N-Queen 문제
# - (y,x) 좌표에 queen 을 놓은 적이 있다.
# - visited 기록 방법
#   - 1. 이차원 배열
#   - 2. 일차원 배열을 효율적으로 하는 방법
# if abs(visited[row] - visited[col]) == abs(row - col):
#     return False

# level: 재귀가 언제까지 돌아야 할까?
# branch: N개의 열
def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가
    for i in range(row):
        if visited[i][col]:
            return False
    # 2. 왼쪽 대각선 (\)
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1

    # 3. 오른쪽 대각선 (/)
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False
        i -= 1
        j += 1

    return True

def dfs(row):
    global ans
    if row == N:        # 모두 성공한 케이스
        ans += 1
        return

    # 후보군: N개의 열에 대해서
    for col in range(N):    # 가지치기 구간!
        # 기존에 같은 열이나 대각선에 놓았다면 안된다!
        if check(row, col):     # check True일 때만 실행하도록
            visited[row][col] = 1
            dfs(row+1)
            visited[row][col] = 0

N = 8
visited = [[0]* N for _ in range(N)]
ans = 0     # 가능한 정답 수

dfs(0)
print(ans)