T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    word = [list(input()) for _ in range(N)]
    pal_word = []
    # 가로 찾기
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M // 2):
                if word[i][j + k] != word[i][j+M-1-k]:
                    break
            else:
                for j in range(j, j+M):
                    pal_word += word[i][j]
    # 세로 찾기
    for j in range(N):
        for i in range(N-M+1):
            for k in range(M // 2):
                if word[i+k][j] != word[i+M-1-k][j]:
                    break
            else:
                for i in range(i, i+M):
                    pal_word += word[i][j]
    print(f"#{tc} {''.join(pal_word)}")