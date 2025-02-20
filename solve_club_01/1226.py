# 미로 탐색
def run_maze(i, j):
    visited = [[0]*16 for _ in range(16)]
    q = []
    q.append([i, j])
    visited[i][j] = 1
    while q:
        ti, tj = q.pop(0)
        if maze[ti][tj] == 3:
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti+di, tj+dj
            # 미로 안에~ 벽도 아니고~ 방문한 적도 없으면
            if 0<=wi<16 and 0<=wj<16 and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1
    return 0

# 시작점 찾기
def where_s(arr):
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                return i, j

T = 10
for _ in range(1, T+1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]      # 미로 만들기
    s_i, s_j = where_s(maze)     # 시작점
    result = run_maze(s_i, s_j)
    print(f"#{tc} {result}")