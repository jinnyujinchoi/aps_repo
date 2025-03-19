def bfs(start_node):
    q = [start_node]
    while q:
        now = q.pop(0)
        print(now, end=' ')

        for next_node in graph[now]:
            if visited[next_node]:
                continue
            visited[next_node] = 1
            q.append(next_node)

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = list(map(int, input().split()))   # 간선
    S, G = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)

    visited = [0]*(N+1)
    visited[1] = 1
    bfs(1)