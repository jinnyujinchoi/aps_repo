for tc in range(1, 11):  # 테스트 케이스
    dc = int(input())   # dump_count
    box = list(map(int, input().split()))   # 상자 배열
    COUNTS = [0]*101 # 계수 정렬 시작
    for h in box:
        COUNTS[h] += 1 # COUNTS 배열 완
    # 최고점, 최저점 찾기
    for i in range(100, -1, -1): # 역순으로 탐색
        if COUNTS[i] > 0:
            high_val = i
            break
    for i in range(101):
        if COUNTS[i] > 0:
            low_val = i
            break
    # 덤프 반복
    for _ in range(dc):
        if high_val - low_val <= 1: # 차이 1 이하는 중단
            break
        COUNTS[high_val] -= 1 # 최댓값 덤프
        COUNTS[high_val-1] += 1 # 아래로 이동
        if COUNTS[high_val] == 0: # 이전 최댓값 없으면
            high_val -= 1 # 최댓값 재할당

        COUNTS[low_val] -= 1 # 최솟값 덤프
        COUNTS[low_val+1] += 1 # 위로 이동
        if COUNTS[low_val] == 0: # 이전 최솟값 없으면
            low_val += 1 # 최솟값 재할당

    differ_val = high_val - low_val
    print(f"#{tc} {differ_val}")