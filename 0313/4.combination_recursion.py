arr = ['A', 'B', 'C', 'D', 'E']
n = 3       # 3개 뽑을거야
path = []

# 5명 중 3명 뽑는 문제
def recur(cnt, start):
    if cnt == n:        # n명 뽑았을때
        print(*path)    # 다 출력할거야
        return

    # 5명을 고려해야 한다.
    # start : 이전 재귀로부터 넘겨 받아야 하는 값
    for i in range(start, len(arr)):
        path.append(arr[i])
        # i: i번째를 뽑겠다
        # i+1 매개변수 전달 : 다음 재귀 부터는 i+1로 고려
        recur(cnt+1, i+1)
        path.pop()

recur(0, 0)