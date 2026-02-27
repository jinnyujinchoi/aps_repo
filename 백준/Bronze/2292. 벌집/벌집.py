# 1, (2~7)6, (8~19)12, (20~37)18, (38~61)24
N = int(input())
layer = 1
end_num = 1 # 끝 숫자

# N까지 만들어 보자
while N > end_num:
    end_num += layer*6
    layer += 1
print(layer)