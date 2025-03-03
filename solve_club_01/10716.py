# 후위표기법 계산 함수
def postfix(txt):
    s = []
    for i in range(len(txt)):
        if txt[i] == '.':     # .이고
            if len(s) == 1:   # 스택 안 요소가 하나이면
                return " ".join(map(str, s))    # 반환
            else:
                return "error"  # 하나가 아니면 에러
        # 사칙연산이면
        elif txt[i] in "/*+-":  # 사칙연산자 중 하나인데
            if len(s) < 2:      # 요소가 두 개 미만이면
                return "error"  # 에러
            b = s.pop()         # 첫 번째로 pop할 값 -> s[-1]
            a = s.pop()         # 두 번째로 pop할 값 -> s[-2]
            if txt[i] == '/':   # 나누기면 나누기
                s.append(a/b)
            elif txt[i] == '*':   # 곱하기면 곱하기
                s.append(a*b)
            elif txt[i] == '+':   # 더하기면 더하기
                s.append(a+b)
            elif txt[i] == '-':   # 빼기면 빼기
                s.append(a-b)
        else:                       # 숫자면 int 변환시켜 append
            s.append(int(txt[i]))
    return "error"  # 에러 반환

T = int(input())
for tc in range(1, T+1):
    txt = input().split()
    print(f"#{tc} {postfix(txt)}")