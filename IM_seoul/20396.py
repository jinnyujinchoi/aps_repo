T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 돌 개수 / 뒤집기 횟수
    stone = list(map(int, input().split()))  # 초기 상태
    for _ in range(M):
        k, j = map(int, input().split())   # k:기준점, j:뒤집기 시행 개수
        for i in range(k, k+j-1):
            if i < N:   # i가 범위에서 벗어나지 않으면
                if stone[k-1] == 1: # 기준점이 1이면
                    stone[i] = 1
                else:       # 기준점이 0이면
                    stone[i] = 0

    print(f"#{tc}", *stone)