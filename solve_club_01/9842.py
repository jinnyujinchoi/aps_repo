def pre_order(n):
    global cnt
    if n:           # 0번이 아니면, 실존하는 자식이면
        cnt += 1
        pre_order(ch1[n])
        pre_order(ch2[n])

def pre_order2(n):      # 서브트리에 속한 정점 수 리턴
    if n == 0:          # 실존하지 않는 정점이면
        return 0
    else:
        l = pre_order2(ch1[n])      # 왼쪽 서브트리의 정점 수
        r = pre_order2(ch2[n])      # 오른쪽 서브트리의 정점 수
        return l+r+1                # 왼쪽+오른쪽+나 추가

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())        # 간선개수 노드N
    arr = list(map(int, input().split()))

    V = E+1         # 마지막 노드 번호
    ch1 = [0]*(V+1)     # 부모 인덱스 자식1 저장
    ch2 = [0]*(V+1)     # 자식2

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:             # 자식 1이 아직 없으면
            ch1[p] = c
        else:
            ch2[p] = c

    cnt = pre_order2(N)
    print(f"#{tc} {cnt}")