import sys
sys.stdin = open("graph.txt", "r")

# 크루스칼
# - 모든 간선들을 보고
#   - 가중치가 작은 간선부터 고르자 (정렬)
#   - 싸이클이 발생한다면? pass

def find_set(x):    # 대표자 찾기
    if x == parents[x]:
        return x

    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)
    # 싸이클 방지
    if ref_x == ref_y:
        return
    # 일정한 규칙으로 연결하기
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


V, E = map(int, input().split())
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    # 간선에 대한 정보들 저장
    edges.append((s, e, w))

edges.sort(key=lambda x: x[2])    # 가중치 기준으로 오름차순
parents = [i for i in range(V)]     # make_set(정점 기준으로 만들어줌)

# 작은 것부터 고르면서 나아가자
# N-1개를 선택할 때 까지 반복
cnt = 0         # 현재까지 선택한 간선의 수
result = 0     # MST 가중치 합

for u, v, w in edges:
    # u와 v가 연결이 안되어있으면 선택
    # == 다른 집합이라면
    if find_set(u) != find_set(v):
        union(u, v)
        cnt += 1
        result += w

        if cnt == V-1:  # MST 구성 종료
            break

print(result)
