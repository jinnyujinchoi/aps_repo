# 6개의 원소(1~6)이 존재하는 경우

# 1. 각 집합을 만들어 주는 함수
def make_set(x):
    # 1~n 까지의 원소가 있다고 가정 -> 총 n개의 집합을 생성
    # --> 각 원소의 부모(!=대표자)를 자신으로 초기화
    parents = [i for i in range(N+1)]
    ranks = [0]*(N+1)   # rank를 모두 0으로 초기화
    return parents, ranks

# def find_set(x):
#     # 자신 == 부모노드 -> 해당 집합의 대표자다
#     if parents[x] == x:
#         return x
#     # x의 부모노드를 기준으로 다시 대표자를 검색
#     return find_set(parents[x])

# 경로 압축 추가한 .find_set
# def find_set(x):
#     if parents[x] == x:
#         return x
#     # 경로 압축 (path compression)를 통해
#     # x의 부모를 대표자로 변경
#     parents[x] = find_set(parents[x])
#
#     return parents[x]

# 할 때마다, 모든 노드의 대표자 변경하기
def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y):
    # x, y의 대표자를 검색
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 만약 이미 같은 집합이라면..?
    # -> 끝!
    if ref_x == ref_y:
        return

    # 다른 집합이라면 합친다
    # -> 문제에 따라 우선되는 집합으로 합쳐주면 된다.
    # --> 이번 예시: 더 작은 노드로 합친다.
    # if ref_x < ref_y:
    #     parents[ref_y] = ref_x
    # else:
    #     parents[ref_x] = ref_y

    # rank 가 작은 쪽으로 병합
    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:
        # rank 가 같으면 한 쪽으로 병합하고, 대표자의 rank추가
        parents[ref_y] = ref_x
        ranks[ref_x] += 1


N = 6
parents, ranks = make_set(N)

union(1, 3)
union(2, 3)
union(5, 6)
print(parents)

# 3과 5는 같은 집한인가요 ??
if find_set(3) == find_set(5):
    print("같은 집합입니다.")
else:
    print("다른 집합입니다.")