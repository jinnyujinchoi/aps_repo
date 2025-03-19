import sys
sys.stdin = open("graph.txt", "r")

def dfs(node):
    # 보통 그래프 문제들에서
    # K개의 노드를 방문했다면~
    # 어쩌고 했따면~ 조건이 붙을것
    print(node, end=" ")
    # 재귀호출 임에도 기저 조건이 없다
    # 현재 노드에서 인접한 노드들을 모두 확인하며, 한 군데로 진행
    for next_node in graph[node]:
        # 이미 방문했다면 가지마라
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)

N, M = map(int, input().split())
# 1. 그래프 저장하기
#   - 비어있는 그래프 생성
#   - 그래프 정보 입력받기
# graph = [[0]* (N+1) for _ in range(N+1)]   # 인접 행렬

# 인접 리스트
graph = [[]for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)  # 양방향이면 , 뒤집어서 저장

visited = [0]*(N+1)
visited[1] = 1
dfs(1)