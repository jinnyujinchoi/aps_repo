# 큐 생성
queue = [0] * 3     # 세 칸 짜리 큐
front = rear = -1   # 처음엔 -1로 초기화
print(queue)

# 1, 2, 3 인큐!
rear += 1           # enqueue 1
queue[rear] = 1
print(queue)

rear += 1           # enqueue 2
queue[rear] = 2
print(queue)

rear += 1           # enqueue 3
queue[rear] = 3
print(queue)

# 1, 2, 3 데큐!
while front != rear:    # 큐에 원소가 남아있으면
    front += 1          # dequeue 1
    print(queue[front])

    front += 1
    print(queue[front]) # dequeue 2

    front += 1
    print(queue[front]) # dequeue 3

