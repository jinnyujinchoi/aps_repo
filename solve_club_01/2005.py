# 파스칼 삼각형을 저장할 2차원 배열
p = [[] for _ in range(10)]
for i in range(10): # N의 크기는 10까지
    for j in range(i+1):  # 각 열은 i보다 하나 큰 값까지
        if j == 0 or i == j:  # 첫 번째 열이거나, 마지막 열이면
            p[i].append(1)
        else:
            # 왼쪽 위 값 + 오른쪽 위 값
            p[i].append(p[i-1][j-1] + p[i-1][j])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f"#{tc}")
    for i in range(N):
        print(*p[i])    # 리스트 빼고 출력