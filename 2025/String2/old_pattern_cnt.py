def bruteforce_cnt(p, t):       # 패턴의 등장 횟수 리턴
    N = len(t)
    M = len(p)
    i = j = 0
    cnt = 0
    while i < N:      # 벗어났다고 중단ㄴ
        if t[i] != p[j]:  # 두 원소 다르면
            i = i - j + 1  # i-j 비교를 시작했던 위치
            j = 0
        else:  # 원소 같으면
            i += 1
            j += 1
        if j==M:        # 패턴을 찾은 경우
            cnt += 1
            i = i-j+1   # 패턴 끝난 지점 다음 위치
            j = 0       # 패턴 처음으로 다시 돌아가!
    return cnt

t = 'TTTTTATTAATA'
p = 'AT'
print(bruteforce_cnt(p, t))