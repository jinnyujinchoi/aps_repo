"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
def dfs(v, N):      # v 출발, N 마지막 정점
    visited = [0]*(N+1)     # 방문 표시
    stack = []      # 스택

    while True:
        if visited[v] == 0:     # 첫 방문이면
            visited[v] = 1
            print(v)
        # v에 인접하고 방문 안한 w가 있으면
        for w in adj_list[v]:   # v 행에 있는 애들 꺼내봐!
            if visited[w] == 0:     # 방문하지 않았으면
                stack.append[v]     # 현재 정점 push
                v = w           # w로 이동
            break        # for w 브레이크
        else:               # 더 이상 갈 곳이 없는 경우
            if stack:       # pop
                v = stack.pop()
            else:           # 스택이 비어 있으면
                break       # while True:

V, E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]     # 인접 리스트

for i in range(E):      # 두 개씩 읽어오기
    v, w = graph[i*2], graph[i*2+1]
    adj_list.append(w)
    adj_list.append(v)      # 방향이 없는 경우

dfs(1, V)       # 1부터 탐색..?