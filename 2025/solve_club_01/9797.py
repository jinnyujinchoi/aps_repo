# 탐색 시작
def bfs(S, G, N):
    visited = [0]*(N+1)                 # 1부터이므로 N+1
    q = []
    q.append(S)
    visited[S] = 1
    while q:
        t = q.pop(0)
        if t == G:   # 노드가 도착점이 되면
            return visited[t] -1   # 도착점까지의 거리 리턴
        for i in adj_l[t]:          # 인접리스트 순회
            if visited[i] == 0:         # 방문한 적이 없으면
                q.append(i)             # 인큐
                visited[i] = visited[t] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())        # 노드 수 / 간선 수
    adj_l = [[] for _ in range(V+1)]        # 인접리스트 만들기, 노드는 1부터 이므로 V+1
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj_l[n1].append(n2)                # 방향성이 없는 경우
        adj_l[n2].append(n1)
    S, G = map(int, input().split())        # 시작 노드, 끝 노드

    result = bfs(S, G, V)
    print(f"#{tc} {result}")