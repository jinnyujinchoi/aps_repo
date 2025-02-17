def dfs(v):      # S 출발, G 마지막 정점
    stack = []      # 스택

    while True:
        # if visited[v] == 0:   # 조건에 따라 생략 가능
        visited[v] = 1  # v에 방문 표시
        if v == G:
            return 1
        # S에 인접한 정점 중 방문 안한 정점 w가 있으면
        for w in adj_list[v]:   # 인접한 정점 w을 꺼내서
            if visited[w] == 0: # 방문한 적이 없으면
                stack.append(v)  # push v
                v = w  # w 에 방문
                break   # for w    # 다른 인접 정점 확인 중단 break
        else:       # 더 이상 인접한 곳이 없으면
            if stack:   # 최근에 지나온 정점으로 복귀, 지나온 정점이 있어야 함!
                v = stack.pop()  # 마지막 원소 반환
            else:
                break           # while True
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(E)]
    adj_list = [[] for _ in range(V+1)]     # 인접 리스트

    for i in range(E):      # 두 개씩 읽어오기
        adj_list[graph[i][0]].append(graph[i][1])
    # for n1, n2 in graph:
    #     adj_list[n1].append(n2)
    S, G = map(int, input().split())
    visited = [0]*(V+1)

    # S부터 탐색 후, visited[0]에 방문한 적이 있으면 성공
    print(f"#{tc} {dfs(S)}")