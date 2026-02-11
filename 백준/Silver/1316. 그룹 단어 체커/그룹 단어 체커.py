N = int(input())
cnt = 0
for _ in range(N):
    word = list(input())
    passed = [] # 이전에 나온 문자 리스트
    prev = word[0]
    isDuplicated = False # 중복 여부 검사
    for i in range(1, len(word)):
        # 이전 문자와 다른데,
        if word[i] != prev:
            passed.append(prev) # 지나간 문자 추가
            # passed에 값이 존재한다면
            if word[i] in passed:
                isDuplicated = True  # 플래그 false
                break # 그만!
        prev = word[i]

    if not isDuplicated:
        cnt += 1

print(cnt)