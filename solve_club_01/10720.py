# 승자는 누구
def winner(arr, N):
    s = [i for i in range(N)]   # 학생 등번호 스택에 추가
    while len(s) > 1:           # 하나 남을 때까지 반복
        next = []               # 다음 라운드 스택 생성
        while len(s) > 1:       # 최소 두 명 있으면
            a = s.pop(0)            # 첫 번재 학생 pop
            b = s.pop(0)            # 두 번째 학생 pop
            if arr[a] == arr[b]:    # 비기면
                next.append(a)         # 인덱스 작은 순 append
            else:
                if arr[a] == 1 and arr[b] == 3:   # 가위vs보
                    next.append(a)
                elif arr[a] == 1 and arr[b] == 2:   # 가위vs바위
                    next.append(b)
                elif arr[a] == 2 and arr[b] == 1:   # 바위vs가위
                    next.append(a)
                elif arr[a] == 2 and arr[b] == 3:   # 바위vs보
                    next.append(b)
                elif arr[a] == 3 and arr[b] == 1:   # 보vs가위
                    next.append(b)
                elif arr[a] == 3 and arr[b] == 2:   # 보vs바위
                    next.append(a)
        if s:   # 다 돌았는데 마지막 한 명 있으면
            next.append(s.pop(0))   # 부전승 추가
        s = next                    # 다음 라운드
    return s[0]+1   # 인덱스+1 반환

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    print(f"#{tc} {winner(card, N)}")