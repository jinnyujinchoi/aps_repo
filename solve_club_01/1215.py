def find_palindrome(word, M):
    cnt = 0     # 회문 개수
    # 가로 찾기
    for i in range(8):
        for j in range(8-M+1):
            for k in range(M//2):
                if word[i][j+k] != word[i][j+M-1-k]:
                    break
            else:
                cnt += 1
    # 세로 찾기
    for j in range(8):
        for i in range(8-M+1):
            for k in range(M//2):
                if word[i+k][j] != word[i+M-1-k][j]:
                    break
            else:
                cnt += 1
    return cnt

for tc in range(1, 11):
    M = int(input())        # 회문 길이
    word = [input() for _ in range(8)]
    print(f"#{tc} {find_palindrome(word, M)}")