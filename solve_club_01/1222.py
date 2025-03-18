for tc in range(1, 11):
    N = int(input())
    txt = input()

    equ = ''    # 후위식 저장 문자열
    s = []      # 빈 스택 생성
    # 후위 표기 변경
    for ch in txt:
        if ch.isdigit():    # 숫자이면
            equ += ch
        else:
            while s:        # 스택 안 요소 있으면
                equ += s.pop()  # 스택 요소 먼저 추가
            s.append(ch)        # 현재 요소 스택에 추가
    while s:
        equ += s.pop()          # 다 돌았는데 남으면 추가
    # 후위 계산
    for ch in equ:
        if ch.isdigit():    # 숫자이면
            s.append(int(ch))
        else:               # +이면
            op2 = s.pop()
            op1 = s.pop()
            if ch == '+':
                s.append(op1 + op2)
    # 마지막 값 반환
    print(f"#{tc} {s.pop()}")