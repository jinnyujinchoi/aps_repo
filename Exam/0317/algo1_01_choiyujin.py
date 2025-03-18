T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # 배열 길이 / '1'의 개수
    bin = list(map(int, input()))       # 이진수 배열

    ans = 0
    for i in range(N):      # 전체 돌면서 조건 만족하는 수 찾기
        one_cnt = 0         # 1의 개수가 K를 만족하지 못할 경우를 대비한, 1의 개수
        if bin[i] == 1:     # i가 1일 때, 시작
            cnt = 0             # 길이 초기화
            KK = K              # K를 따로 담을 변수
            for j in range(i, N):
                if bin[j] == 1:     # 값이 1이면,
                    KK -= 1          # k 값 1 감소
                    one_cnt += 1     # 1 개수 증가
                cnt += 1             # 길이도 증가
                if KK == 0:         # KK 소진시 브레이크
                    break
            if ans < cnt:
                ans = cnt
                if one_cnt < K:     # cnt가 최대일 때, 1의 개수가 K보다 작으면
                    ans = 0         # 결과는 0

    print(f"#{tc} {ans}")