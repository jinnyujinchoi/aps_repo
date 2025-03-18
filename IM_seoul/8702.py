T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    min_differ = 190    # 차이 최댓값 할당
    for k in range(1, N): # k는 기준점 / 기준점 범위 내 반복
        front_val = back_val = 0    # 당근 수확량 초기화 각각
        for j in range(k):
            front_val += carrot[j]
        for j in range(k, N):
            back_val += carrot[j]
        differ = abs(front_val-back_val)
        if min_differ > differ:
            min_differ = differ
            carrot_idx = k
    print(f"#{tc} {carrot_idx} {min_differ}")