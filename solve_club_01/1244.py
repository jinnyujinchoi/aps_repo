def f(i, N, M):
    global max_v
    if i==N:        # 주어진 교환 횟수 사용
        tmp = int(''.join(card))
        if max_v < tmp:     # 모든 교환 끝났을 때, 최댓값 반환
            max_v = tmp
    else:


T = int(input())
for tc in range(1, T+1):
    num, N = input().split()
    card = list(num)    # 카드 리스트
    N = int(N)      # 교환 횟수
    M = len(card)
    max_v = 0       # 최대 상금
    f(0, N, M)