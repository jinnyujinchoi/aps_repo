def enq(n):
    global last
    last += 1       # 마지막 정점 추가(완전 이진 트리를 유지하기 위해서)
    heap[last] = n

    c = last        # 최소힙 -> 부모 < 자식 항상!
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]     # 자리 바꾸기
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    last = 0                                # 마지막 노드(아직 없으니까 0으로 초기화)

    heap = [0]*(N+1)                        # 힙 생성
    for x in arr:
        enq(x)

    ans = 0         # 합 초기화
    p = last // 2   # p는 last의 부모
    while p:        # 부모가 존재하면(0번 정점이 아니면 부모 정점)
        ans += heap[p]
        p //= 2     # 부모의 부모로 이동(부모가 존재할 때 까지!)

    print(f"#{tc} {ans}")