import sys
sys.stdin = open("graph.txt", "r")

# prim
#   - 특정 정점 기준 시작
# - 갈 수 있는 노드들 중 가중치가 작은 노드부터
# - 그냥 큐가 아닌, 우선순위 큐

def prim(s_node):
    pq = [(0, s_node)]     # 우선순위큐 생성 / s_node까지 갈 때 0만큼 가중
    # 종료 조건: N개를 모두 연결했을 때
    MST = [0] * V   # visited랑 동일
    min_w = 0       # 최소 비용 저장

    while pq:
        w, node = heapq.heappop(pq)

        # 이미 방문한 노드를 뽑았다면 continue (재방문 방지)
        if MST[node]:
            continue

        MST[node] = 1       # 방문 처리
        min_w += w          # 누적합 추가

        for next_node in range(V):
            # 갈 수 없으면 pass
            if graph[node][next_node] == 0:
                continue
            # 이미 방문했으면 pass
            if MST[next_node]:
                continue

            heapq.heappush(pq, (graph[node][next_node], next_node))

    return min_w


import heapq

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]     # 인접 행렬

for _ in range(E):
    s, e, w = map(int, input().split()) # start/ end / weight
    # 양방향
    graph[s][e] = w
    graph[e][s] = w

result = prim(0)    # 정점을 바꿔도 결과는 동일 (왜? 최소 비용은 보장됨)
print(f"최소 비용 = {result}")