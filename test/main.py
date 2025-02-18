# 공굴리기 함수 선언
def cross_build(arr, N):
    cnt = 1     # 이동 횟수 초기화(본인 자리 포함)
    cnt_list = []   # 횟수 리스트
    for i in range(N):
        for j in range(N):
            while True:
                chk = arr[i][j]
                new_i, new_j = i, j
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < N:     # 배열 넘지 않을 때
                        if arr[ni][nj] < chk:     # 출발위치보다 값이 작을 때
                            chk = arr[ni][nj]
                            new_i, new_j = ni, nj
                if chk != arr[i][j]:
                    cnt += 1
                    i, j = new_i, new_j
                else:
                    break
            cnt_list.append(cnt)    # 현재 이동횟수 추가
            cnt = 1

    # 이동횟수 반환
    return cnt_list

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    build = [list(map(int, input().split())) for _ in range(N)]   # 빌딩 높이 받기
    print(f"#{tc} {cross_build(build, N)}")
