def KFC(num):
    # 재귀호출 중지
    if num == 5:
        return
    print(num)
    KFC(num + 1)

KFC(0)
print("끝")