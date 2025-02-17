T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 팀원수 / 명령 횟수 받기
    flag = list(map(int, input().split()))      # 팀원 배치
    for _ in range(M):  # 명령 횟수 만큼 반복
        a, b, c = map(int, input().split())     # 난이도/기준번호/명수 받기
        for i in range(b-1, b+c-1):     # 기준번호부터 c명까지
            if i < N:
                if flag[i] == 0:    # 내렸으면 올리고
                    flag[i] = 1
                else:   # 올렸으면 내리고
                    flag[i] = 0

    print(f"#{tc}", *flag)  # 결과 출력