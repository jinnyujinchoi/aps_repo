T = int(input())
for tc in range(1, T+1):
    board = list(input())
    total_bar = 0  # 저장된 막대 개수
    recent_bar = 0  # 현재 막대 개수
    # 레이저로 잘라주기
    for i in range(len(board)):
        if board[i] == '(' and board[i] == board[i+1]:   # 막대의 시작점이면
            recent_bar += 1
        elif board[i] == ')' and board[i] == board[i-1]:  # 막대의 끝점이면
            total_bar += 1
            recent_bar -= 1
        elif board[i] == '(' and board[i+1] == ')':
            total_bar += recent_bar
    print(f"#{tc} {total_bar}")