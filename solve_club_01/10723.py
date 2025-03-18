
# 미로 탈출
def run_maze(i, j, N):  # 시작위치 i,j / 배열 크기
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append([i, j])            # 시작점 인큐하고
    visited[i][j] = 1         # 방문 표시
    while q:                    # 큐가 빌 때까지 반복
        ti, tj = q.pop(0)
        if maze[ti][tj] == 3:     # 도착지에 도착하면!
            return visited[ti][tj] - 2
        # 다음 위치로 가자
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = di+ti, dj+tj
            # 범위도 안 벗어나고, 벽도 아니고, 마지막은 maze에서가 아니고! 들렸던데가 아니면!!!!!!
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1
    return 0

# 시작위치 찾기
def where_s(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:      # 출발 지점이면!
                return i, j          # 그 지점 반환

T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 미로의 크기 -> 2차원 배열 생성하기!
    maze = [list(map(int, input())) for _ in range(N)]      # 미로 생성

    s_i, s_j = where_s(maze, N)     # 시작위치 변수
    result = run_maze(s_i, s_j, N)  # 결과 담기
    print(f"#{tc} {result}")        # 결과 출력