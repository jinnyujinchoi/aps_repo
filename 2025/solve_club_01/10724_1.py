T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    queue = [0] * (N + 1)
    front = 0
    rear = 0
    i = 0
    idx = [0] * (N + 1)

    while True:
        if (rear + 1) % (N + 1) != front:
            rear = (rear + 1) % (N + 1)
            queue[rear] = C[i]
            i += 1
            idx[rear] = i
        elif (rear + 1) % (N + 1) == front:
            rear = (rear + 1) % (N + 1)
            queue[rear] = queue[rear] // 2
            front = (front + 1) % (N + 1)
            if queue[rear] == 0 and rear != 0 and i < M:
                queue[rear] = C[i]
                i += 1
                idx[rear] = i
        if queue == [0] * (N + 1):
            print(f'#{tc} {idx[rear]}')
            break