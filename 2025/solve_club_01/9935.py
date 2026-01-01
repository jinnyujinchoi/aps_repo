def dock(arr):
    arr.sort(key=lambda x: x[1])    # 종료시간 기준으로 sort
    end_t = arr[0][1]               # 첫 화물차의 종료시간
    cnt = 1                         # 화물차 수
    for i in range(1, N):
        if end_t <= arr[i][0]:      # 첫 종료시간보다 (시작시간이) 크다면
            cnt += 1            # 화물차 수 추가
            end_t = arr[i][1]  # 종료시간 변경

    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = []           # 화물차 시간 배열
    for _ in range(N):
        s, e = map(int, input().split())
        time.append([s, e])

    print(f"#{tc} {dock(time)}")
