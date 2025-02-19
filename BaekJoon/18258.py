import sys
input = sys.stdin.readline

def command(order):
    global q
    global front
    global rear
    if order[:4] == 'push':
        p, p_num = order.split()
        rear += 1
        q[rear] = p_num
    if order == 'front':        # 명령이 front
        if front != rear:
            print(q[front+1])
        else:
            print(-1)
    if order == 'back':       # 명령이 back
        if front != rear:
            print(q[rear])
        else:
            print(-1)
    if order == 'size':       # 명령이 size
        print(rear-front)
    if order == 'empty':      # 명령이 empty
        if front != rear:
            print(0)
        else:
            print(1)
    if order == 'pop':        # 명령이 pop
        if front != rear:
            print(q[front+1])
            front += 1
        else:
            print(-1)

front = rear = -1
T = int(input())
q = [0]*T
for _ in range(T):
    order = input().rstrip()
    command(order)
