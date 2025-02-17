# 회문 검사
def palindrome(txt):
    for i in range(len(txt) // 2):
        if txt[i] != txt[len(txt) - (1 + i)]:
            return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    txt = input()
    result = palindrome(txt)
    print(f"#{tc} {result}")