# 미로 탈출 가능~~~~?
def escape(i, j):
    visited = [[0]*N for _ in range(N)]
    q = []      # 큐 생성
    q.append([i, j])
    visited[i][j] = 1
    while q:
        ti, tj = q.pop()
        if maze[ti][tj] == 3:
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti + di, tj + dj
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[wi][wj] + 1
    return 0

# 시작 위치 찾기
def where_s(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    s_i, s_j = where_s(maze, N)
    result = escape(s_i, s_j)
    print(f"#{tc} {result}")