# 반복문자 지우는 함수
def erase(txt):
    top = -1
    s = [0] * len(txt)  # 스택 생성
    i = 0
    while i < len(txt):  # 문자열 끝까지 가면 종료
        top += 1
        s[top] = txt[i]
        i += 1
        if top != -1 and s[top] == s[top - 1]:  # 새로 넣은 문자열이 앞과 같으면
            top -= 2  # 두 문자 동시에 제거
    return top + 1


T = int(input())
for tc in range(1, T + 1):
    txt = input()
    print(f"#{tc} {erase(txt)}")