'''
0과 1로 이루어진 1차 배열에서 7개씩 수를 묶어, 10진수로 출력하기

0000000111100000011000000111100110000110000111100111100111111001100111

answer: 0 120 12 7 76 24 60 121 124 103
'''

def bin_dec(bin_str):
    decimal_number = 0  # 십진수 반환해줄 변수
    power = 0       # 제곱수

    for digit in reversed(bin_str):
        if digit == '1':
            decimal_number += 2**power
        power += 1

    return decimal_number

word = input().strip()

for i in range(0, len(word), 7):
    print(bin_dec(word[i:i+7]), end=' ')