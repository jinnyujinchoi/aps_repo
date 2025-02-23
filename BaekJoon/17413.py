import sys

top = -1
def spop(s):
    global top
    while top >= 0:  # 현재 쌓인 스택 내부에서 반복
        top -= 1  # top 감소
        t = s.pop(top + 1)  # 맨 위 요소 pop
        print(t, end="")  # 추가

def flip(txt):                  # 문자열 뒤집는 함수
    s = [' ']*len(txt)              # 스택 생성 / 문자열 길이는 10만 이하
    # 스택에 문자 넣어 주기
    global top
    i = 0
    while i < len(txt):
        # 소문자거나 숫자이면, 뒤집어서 넣어주기(스택)
        if txt[i] != '<' and txt[i] != '>' and txt[i] != ' ': # 소문자/숫자이면
            top += 1            # top 증가
            s[top] = txt[i]     # 해당 문자/숫자 스택에 추가
        # 공백을 만나면 스택 안 모요소 빼주기
        if txt[i] == ' ':       # 공백을 만나면
            spop(s)
            print(txt[i], end="")
        # 괄호를 만나면 스택 안 요소 뒤집어서 빼주기
        if txt[i] == '<':         # 문자가 '<'이고
            spop(s)
            while txt[i] != '>':
                print(txt[i], end="")
                i+=1
            print(txt[i], end="")
        i+=1
    spop(s)

txt = sys.stdin.readline().rstrip()     # 문자열 받기
flip(txt)    # 문자열 출력