def press_key(p, t):
    N = len(t)  # 전체 문자열 길이
    M = len(p)  # 패턴 길이
    i = j = 0
    t_cnt = N    # not 패턴 길이 셀 거
    p_cnt = 0    # 패턴 길이 셀거
    while i < N:
        if t[i] != p[j]:  # 두 원소 다르면
            i = i - j + 1
            j = 0
        else:  # 원소 같으면
            i += 1
            j += 1
        if j == M-1:  # 패턴을 찾은 경우
            t_cnt -= M
            p_cnt += 1
            i = i + 1  # 패턴 끝난 지점 다음 위치
            j = 0  # 패턴 처음으로 다시 돌아가!
    # 패턴 반복횟수 + 불일치 인덱스
    return p_cnt + t_cnt

T = int(input())
for tc in range(1, T + 1):
    t, p = input().split()
    print(f"#{tc} {press_key(p, t)}")