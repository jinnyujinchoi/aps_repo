import sys
sys.stdin = open("graph.txt", "r")

def bfs(start_node):
    # q에 들어가는 노드들의 의미 : 다음에 방문해야 할 노드들(대기열)
    q = [start_node]    # 시작점 넣은 상태로 출발

    while q:
        # 1. 가장 앞에 있는 노드 뽑기
        # 2. 해당 노드에서 갈 수 있는 노드 큐에 넣기
        now = q.pop(0)
        print(now, end=' ')

        # 인접한 노드를 확인하며
        for next_node in graph[now]:
            # 방문했으면 pass
            if visited[next_node]:
                continue

            visited[next_node] = 1
            q.append(next_node)


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited[1] = 1
bfs(1)