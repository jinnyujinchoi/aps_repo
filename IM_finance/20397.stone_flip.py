T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())       # 돌 개수 / 뒤집기 횟수 받기
    stone = list(map(int, input().split()))

    # 뒤집기 시작
    for _ in range(M):
        k, j = map(int, input().split())    # 기준점, 개수 받기
        for i in range(N):
            if i == k-1:   # i가 기준점 일 때,
                for c in range(1, j+1):  # 확인할 돌 범위
                    if 0<=i-c<N and 0<=i+c<N:
                        if stone[i-c] == stone[i+c]:    # 양 옆 돌이 같으면
                            if stone[i-c] == 0:     # 0이면 1
                                stone[i-c] = 1
                                stone[i+c] = 1
                            else:                   # 1이명 0
                                stone[i-c] = 0
                                stone[i+c] = 0

    # 바뀐 배열 출력
    print(f"#{tc}", *stone)