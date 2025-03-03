def forth(arr):
    s = []
    for i, ch in enumerate(arr):
        if ch.isdigit():    # 숫자이면
            s.append(int(ch))
        elif ch in ('/','*','+','-'):   # 연산자이면
            if len(s) <= 1:
                return "error"
            else:
                op2 = s.pop()
                op1 = s.pop()
                if ch == '/':
                    # 나누기 // 안써서 테케 +34240번 더 돌림...
                    s.append(op1 // op2)
                if ch == '*':
                    s.append(op1 * op2)
                if ch == '+':
                    s.append(op1 + op2)
                if ch == '-':
                    s.append(op1 - op2)
        elif ch == '.':
            if i < len(arr)-1:
                return "error"
            if len(s) == 1:
                return s.pop()
            else:
                return "error"

T = int(input())
for tc in range(1, T+1):
    txt = input().split()
    print(f"#{tc} {forth(txt)}")