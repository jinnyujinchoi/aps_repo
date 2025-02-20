def BFS(G, v, n):       # 그래프 / 탐색 시작점 / 정점의 개수
    visited = [0]*(n+1)
    q = []
    q.append(v)
    visited[v] = 1      # 인큐와 방문 표시를 동시에 진행!
    while q:            # 큐가 비어있지 않을 때!(비워질 때까지 계속 반복할거야~~)
        # 미로의 출구를 탈출하는 법도 이 부분에서!
        t = q.pop(0)                        # 첫번째 원소 반환
        # visit(t)                          # 방문한 정점에서 할 일
        for i in G[t]:                      # t와 연결된 모든 정점에 대해
            if not visited[i]:              # 인큐(방문)되지 않은 곳이라면
                q.append(i)                 # 큐에 넣고
                visited[i] = visited[t] + 1 # 방문하는데 자신의 노드(+1)로 표시하기