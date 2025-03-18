# 그냥 순열(not 중복)

path = []   # 뽑은 카드 저장
used = [False] * 7
# 왜 7개??? 그냥 0번 인덱스 버림
# cnt = 재귀호출마다 누적되어서 전달되어야 하는값
def recur(cnt):
    if cnt == 3:        # 카드는 3개 뽑을거!
        # 종료 시에 호출 해야 할 로직 작성
        print(*path)
        return

    # 만약 카드가 1~6까지 6개라면
    for num in range(1, 7):
        # 이미 num을 뽑았다면 뽑지 마라
        # == num을 뽑지 않았을 때만 뽑아라
        # in은 비효율적!
        # if num in path:
        #     continue

        # 인덱스 검색 연산은 O (1)
        if used[num] is True:
            continue

        used[num] = True
        path.append(num)
        recur(cnt+1)
        path.pop()
        used[num] = False

recur(0)