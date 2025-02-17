T = int(input())
for tc in range(1, T + 1):
    N, word_len = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    puzzle_fit = 0  # fit한 자리수 초기화
    # 행에서 찾기
    for i in range(N):
        one_len = 0  # 연속 1 길이 초기화
        for j in range(N):
            if arr[i][j] == 1:
                one_len += 1
            else:
                if one_len == word_len:
                    puzzle_fit += 1
                one_len = 0
        if one_len == word_len:
            puzzle_fit += 1
    # 열에서 찾기
    for j in range(N):
        one_len = 0  # 연속 1 길이 초기화
        for i in range(N):
            if arr[i][j] == 1:
                one_len += 1
            else:
                if one_len == word_len:
                    puzzle_fit += 1
                one_len = 0
        if one_len == word_len:
            puzzle_fit += 1

    print(f"#{tc} {puzzle_fit}")