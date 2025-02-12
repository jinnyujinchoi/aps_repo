def press_key(p, t):
    N = len(t)  # 전체 문자열 길이
    M = len(p)  # 패턴 길이
    i = j = 0
    p_cnt = 0  # 패턴 반복횟수
    while i < N:
        if t[i] != p[j]:  # 두 원소 다르면
            i = i - j + 1  # i-j 비교를 시작했던 위치
            j = 0
        else:  # 원소 같으면
            i += 1
            j += 1
        if j == M:  # 패턴을 찾은 경우
            p_cnt += 1
            i = i - j + 1  # 패턴 끝난 지점 다음 위치
            j = 0  # 패턴 처음으로 다시 돌아가!
    # 패턴 반복횟수 + (전체 길이 - (패턴길이*패턴 반복횟수))
    return p_cnt + (N - (M * p_cnt))

T = int(input())
for tc in range(1, T + 1):
    t, p = input().split()
    print(f"#{tc} {press_key(p, t)}")