pri = {'*':2, '+':1}    # 우선순위 딕셔너리
s = []  # 스택 생성
# 중위->후위 변경 함수
def pre_post(arr):
    equ = ''    # 후위 표기로 바꿔줄 문자열
    for ch in arr:
        if ch.isdigit():    # 숫자일 경우
            equ += ch
        else:
            # 스택 안 요소o, 연산자 우선순위가 같거나 작을 때
            while s and pri[ch] <= pri[s[-1]]:
                equ += s.pop()  # 먼저 꺼내서 equ에 추가
            s.append(ch)        # 그리고 자신도 추가
    while s:                    # 마지막에도 남아 있다면
        equ += s.pop()          # 모두 꺼내 추가

    return equ

# 후위 계산
def post_cal(arr):
    equ = pre_post(arr)
    for ch in equ:
        if ch.isdigit():    # 숫자이면
            s.append(int(ch))   # 정수형 변환 push
        else:           # 연산자이면
            op2 = s.pop()
            op1 = s.pop()
            if ch == '*':
                s.append(op1 * op2)
            elif ch == '+':
                s.append(op1 + op2)
    # 마지막 값 반환
    return s.pop()

for tc in range(1, 11):
    N = int(input())
    txt = input()
    print(f"#{tc} {post_cal(txt)}")