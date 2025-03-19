# from collections import deque
def bfs(N, M):
    q = [0]*1000000     # 큐 생성  # q = deque(
    front = rear = -1
    visited = [0]*1000001   # visited 생성
    rear += 1
    q[rear] = N
    visited[N] = 1      # 시작점 visited 표시
    while front != rear:    # while q:
        front += 1
        t = q[front]
        if t == M:      # 목표인 경우
            return visited[M] - 1
        # -1, +1, *2, -10인 경우, 백만이하 자연수, 만든 적이 없는
        if t-1 >= 0 and visited[t-1] == 0:    # 자연수이고, 만든적이 없으면
            rear += 1
            q[rear] = t-1
            visited[t-1] = visited[t] + 1
        if t+1 <= 1000000 and visited[t+1] == 0:
            rear += 1
            q[rear] = t+1
            visited[t+1] = visited[t] + 1
        if t*2 <= 1000000 and visited[t*2] == 0:
            rear += 1
            q[rear] = t*2
            visited[t*2] = visited[t] + 1
        if t-10 > 0 and visited[t-10] == 0:
            rear += 1
            q[rear] = t-10
            visited[t-10] = visited[t] + 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    ans = bfs(N, M)
    print(f"#{tc} {ans}")