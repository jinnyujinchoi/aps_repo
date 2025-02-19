# 피자 굽기 함수
def make_pizza(arr, N, M):
    oven = [0]*(N+1)    # 오븐 만들기
    front = rear = 0

    # 피자 넣어주기
    i = 0   # 치즈값 인덱스 초기화
    while front == rear:        # 오븐이 공백인 동안
        rear = (rear+1)%len(oven)
        oven[rear] = arr[i]
        i += 1

    # 치즈 녹이기
    while (rear-front+len(oven))%len(oven) > 1:  # 정수(피자)가 하나 남을 때 까지
        oven[front+1] = oven[front+1]//2  # 꺼낼 피자 녹이기
        if oven[front+1] == 0:    # 꺼낸 피자가 0이 되면
            front = (front+1)%len(oven)  # 피자 제거
        else:   # 0이 아니면
            rear = (rear+1)%len(oven)   # 꺼낸 피자 도로 넣기
            oven[rear] = oven[front]

    # 피자 하나 남았을 때
    if (rear-front+len(oven))%len(oven) == 1:
        return oven[front+1]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 화덕 크기 / 피자 개수
    cheese = list(map(int, input().split()))
    print(f"#{tc} {make_pizza(cheese, N, M)}")