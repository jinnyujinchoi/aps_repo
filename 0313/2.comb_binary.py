arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar):
    print(f'target = {tar}', end=' / ')
    for i in range(n):
        # 각각 원소가 포함되어 있는지 확인
        if tar & 0x1:
            print(arr[i], end='')
        tar >>= 1       # 맨 우측 비트 삭제
                        # == 다음 원소를 확인하겠다.

# 전체 부분집합 확인
for target in range(1<<n):
    get_sub(target)
    print()