# [0,1,2] 3개 카드 존재
# 2개 뽑을 예정

path = []   # 뽑은 카드 저장
# cnt = 재귀호출마다 누적되어서 전달되어야 하는값
def recur(cnt):
    if cnt == 3:
        # 종료 시에 호출 해야 할 로직 작성
        print(*path)
        return

    for num in range(1, 7):
        path.append(num)
        recur(cnt+1)
        path.pop()
    # # 1개 카드 뽑고
    # path.append(0)
    # # 다음 재귀 호출(뽑은 카드 하나 추가)
    # recur(cnt+1)
    # path.pop()
    #
    # path.append(1)
    # recur(cnt+1)
    # path.pop() 
    #
    # path.append(2)
    # recur(cnt+1)
    # path.pop()

# 제일 처음 호출할 때 시점
# 초기값 전달하며 시작
recur(0)