T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    a_arr = list(map(int, input().split()))
    b_arr = list(map(int, input().split()))
    c = []
    i = j = 0
    while i+j < A + B:  # 배열 길이가 A+B가 될 때까지
        if i < A:   # 인덱스가 배열 이내에 있으면
            if a_arr[i]:    # 값이 존재 하면
                c.append(a_arr[i])
                i += 1
        if j < B:   # 인덱스가 배열 이내에 있으면
            if b_arr[j]:   # 값이 존재 하면
                c.append(b_arr[j])
                j += 1

    print(f"#{tc}", *c)