def grow_carrot(arr, N):
    grow_list = []  # 연속 당근 개수 리스트
    cnt = 0     # 연속 당근 횟수
    for i in range(1, N):
        if i < N:
            if arr[i] > arr[i-1]: # i값이 i-1보다 크다면
                cnt += 1
                grow_list.append(cnt+1)
            else:
                grow_list.append(cnt)
                cnt = 0
    # 최댓값 찾기
    max_val = 1     # 연속 없을 경우 1 반환
    for num in grow_list:
        if max_val < num:
            max_val = num
    return max_val

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))
    print(f"#{tc} {grow_carrot(carrot, N)}")
