T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 전등 개수
    start = list(map(int, input().split()))     # 초기 상태
    end = list(map(int, input().split()))       # 끝난 상태
    switch = 0      # 스위치 횟수 초기화
    i = 0
    while i < N:    # 끝까지 다 돌 때까지
        if start[i] != end[i]:
            # 스위치 조작
            for j in range(i, N):   # i번째 부터 끝 스위치까지 조작
                if start[j] == 0:
                    start[j] = 1
                else:
                    start[j] = 0
            switch += 1
        i += 1

    print(f"#{tc} {switch}")