T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    # 딕셔너리에 개수 넣기
    c = {}
    for i in range(len(str1)):
        val_cnt = 0   # val 값 초기화
        for j in range(len(str2)):
            if str2[j] == str1[i]:
                val_cnt += 1
                c[str1[i]] = val_cnt
            else:
                continue
    # 가장 큰거 찾기
    count_num = list(c.values())
    max_val = 0
    for num in count_num:
        if max_val < num:
            max_val = num
    print(f"#{tc} {max_val}")
    # print(f"#{tc} {count_num}")