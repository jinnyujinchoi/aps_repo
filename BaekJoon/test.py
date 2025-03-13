def solve(arr):
    arr.sort(key=lambda x: x[1])    # 종료시간 기준 정렬
    classroom = 1             # 강의실 수 초기화
     # 강의 시작
    end = [arr[0][1]]
    i = 1
    while i < N:
        for idx, end_time in enumerate(end):
            if end_time <= arr[i][0]:
                # 현재 end_time 값을 수정해야 한다.
                end[idx] = arr[i][1]
                i += 1
                break
        else:
            classroom += 1
            end.append(arr[i][1])
            i += 1

    return classroom

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]

print(solve(time))