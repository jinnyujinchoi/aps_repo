T = int(input()) # tc 횟수

def paint(lst, color):
    x1,y1,x2,y2 = lst
    for i in range(x1,x2):
        for j in range(y1,y2):
            paper[i][j] = color

for _ in range(T):
    paper = [[0]* 100 for _ in range(100)] # 빈 종이 생성
    white = list(map(int, input().split())) # 흰 종이 범위
    black_1 = list(map(int, input().split())) # 검은 종이1 범위
    black_2 = list(map(int, input().split())) # 검은 종이2 범위

    paint(white, -1) # 흰 종이 색칠
    paint(black_1, 1) # 검은 종이1 색칠
    paint(black_2, 1) # 검은 종이2 색칠

    x1,y1,x2,y2 = white
    covered = True # 흰 종이가 완전히 덮혔을 때
    for i in range(x1,x2): # 흰 종이 순회
        for j in range(y1,y2):
            if paper[i][j] == -1: # 검은 종이가 덮혔으면
                covered = False
                break
        if not covered:
                break

    print("NO" if covered else "YES")