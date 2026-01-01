T = int(input())
for tc in range(1, T+1):
    N = int(input())    # N개의 양수
    arr = list(map(int, input().split()))   # 양수 배열

    max_idx = 0     # 배열에서 가장 큰 값의 인덱스 초기화
    min_idx = 0     # 배열에서 가장 작은 값 인덱스 초기화
    for i in range(N):
        if arr[max_idx] <= arr[i]: # 가장 큰 값의 가장 큰 인덱스 찾기
            max_idx = i
        if arr[min_idx] > arr[i]: # 가장 작은 값은 가장 작은 인덱스 찾기
            min_idx = i
    # 큰 값에서 작은 값 나눠주기
    if max_idx > min_idx: print(f"#{tc} {max_idx-min_idx}")
    else: print(f"#{tc} {min_idx-max_idx}")