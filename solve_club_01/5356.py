T = int(input())
for tc in range(1, T+1):
    board = [list(input()) for _ in range(5)]
    full_word = []
    max_len = 0
    # 가장 긴 행 찾기
    for i in range(5):
        if max_len < len(board[i]):
            max_len = len(board[i])
    # 공백 넣어주기
    for i in range(5):
        for j in range(max_len-len(board[i])):
            board[i].append('')
    # 글자 뽑아내기
    for j in range(max_len):
        for i in range(5):
            full_word += board[i][j]

    print(f"#{tc} {''.join(full_word)}")