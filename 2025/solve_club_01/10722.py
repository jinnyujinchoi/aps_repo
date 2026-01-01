def rotation(q, N, M):    # 회전하기 함수 / 배열_크기_반복횟수
    front = 0
    rear = N-1
    rear = (rear + M) % N
    front = (front + M) % N
    return q[front]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    print(f"#{tc} {rotation(q, N, M)}")