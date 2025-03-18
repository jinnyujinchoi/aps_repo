# 공굴리기 함수 선언
def cross_build(arr, N):
    cnt = 1     # 이동 횟수 초기화(본인 자리 포함)
    cnt_list = []   # 횟수 리스트
    for i in range(N):
        for j in range(N):
            k, l = i, j
            while True:
                chk = arr[k][l]
                new_k, new_l = k, l
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                    nk, nl = k+di, l+dj
                    if 0 <= nk < N and 0 <= nl < N:     # 배열 넘지 않을 때
                        if arr[nk][nl] < chk:     # 출발위치보다 값이 작을 때
                            chk = arr[nk][nl]
                            new_k, new_l = nk, nl
                if chk != arr[k][l]:
                    cnt += 1
                    k, l = new_k, new_l
                else:
                    break
            cnt_list.append(cnt)    # 현재 이동횟수 추가
            cnt = 1

    # 이동횟수 반환
    return max(cnt_list)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    build = [list(map(int, input().split())) for _ in range(N)]   # 빌딩 높이 받기
    print(f"#{tc} {cross_build(build, N)}")
