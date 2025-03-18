# 전위순회
def pre_order(n):
    global pre_num
    global in_num
    global post_num
    if n <= N:
        pre_num += str(tree[n])
        pre_order(n*2)
        in_num += str(tree[n])
        pre_order(n*2+1)
        post_num += str(tree[n])

# # 중위순회
# def in_order(n):
#     global in_num
#     if n <= N:
#         in_order(n*2)
#         in_num += str(tree[n])
#         in_order(n*2+1)
#
# # 후위순회
# def post_order(n):
#     global post_num
#     if n <= N:
#         post_order(n*2)
#         post_order(n*2+1)
#         post_num += str(tree[n])

# 이진수를 십진수로
def bin_dec(bin_str):
    dcnum = 0           # 십진수 담을 변수
    power = 0           # 지수
    for digit in bin_str[::-1]:
        if digit == '1':
            dcnum += 2**power
        power += 1
    return dcnum

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노드 개수
    tree = [0]+list(map(int, input().split()))

    pre_num = ''
    in_num = ''
    post_num = ''

    pre_order(1)
    # in_order(1)
    # post_order(1)

    pre_num = bin_dec(pre_num)
    in_num = bin_dec(in_num)
    post_num = bin_dec(post_num)

    ans = max(pre_num, in_num, post_num)
    print(f"#{tc} {ans}")