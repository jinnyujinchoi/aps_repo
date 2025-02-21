import sys
input = sys.stdin.readline

# dfs 함수
def dfs(v, N):
    visited = [0]*(N+1)
    s = [v]
    while s:                    # 스택이 빌 때까지
        t = s.pop()             # 마지막 노드 꺼내기
        if visited[t] == 0:     # 방문하지 않았다면
            visited[t] = 1      # 방문 처리
            print(t, end=" ")   # 방문한 곳 출력
            for i in reversed(adj_l[t]):    # 인접 노드 역으로 추가
                if visited[i] == 0:     # 방문안햇다면 추가
                    s.append(i)
    return 0

# bfs 함수
def bfs(v, N):          # 시작점 / 크기
    visited = [0]*(N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:                # 큐가 빌 때까지
        t = q.pop(0)        # 첫 노드 꺼내기
        print(t, end=" ")    # 방문한 곳 출력
        for i in adj_l[t]:
            if visited[i] == 0:
                q.append(i)         # 방문 안했다면 추가
                visited[i] = visited[t] + 1
    return 0

N, M, V = map(int, input().split())    # 정점 수 / 간선 수 / 시작 번호
# 인접 리스트 생성
adj_l = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().rstrip().split())
    adj_l[n1].append(n2)
    adj_l[n2].append(n1)
for i in range(N+1):
    adj_l[i].sort()
# 결과 출력
dfs(V, N)
print()
bfs(V, N)