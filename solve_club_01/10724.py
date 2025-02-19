def rotation_pizza(arr, N, M):      # 치즈 양_화덕 크기_피자 개수 받기
    pass
    oven = []
    front = rear = 0
    while ((rear+1) % len(oven)) != front:       # 다 찰 때까지 피자 넣기!
        for i in range(N):                  # 화덕에 피자 넣기 / i는 피자 번호
            oven[i+1] = arr[i]
            rear = (rear + 1)%len(oven)         # rear 위치 변경
        while len(oven) != 1:               # 남은 피자가 하나일 때 까지
            while oven[1:] != 0:                 # 피자 하나가 다 녹을때 까지
                i = 1
                oven[i] = oven[i]//2             # 치즈를 계속 녹여
                if oven[i] == 0:
                    break                                                                                                                                                                                                                                                                                                                                                                                                                                               

                        if oven[i] == 0:
                            front = i
                            oven.pop(oven[i])           # 다 녹으면 화덕에서 빼기
                            front = (front + oven[i])%len(oven)   # front 위치 변경

    # 마지막 남은 피자 번호 반환
    return front+1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    print(f"#{tc} {rotation_pizza(cheese, N, M)}")