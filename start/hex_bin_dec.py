'''
16진수 문자로 이루어진 1차 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력해 보자

입력
0F97A3


2진수: 000011111001011110100011
answer: 7, 101, 116, 3
'''

def hex_bin(hex_str):
    # 16진수를 2진수로 변환하기 위한 매핑 테이블
    hex_to_bin_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    binary_string = ''.join(hex_to_bin_map[char] for char in hex_string.upper())
    return binary_string


def bin_dec(bin_str):
    decimal_number = 0  # 십진수 반환해줄 변수
    power = 0       # 제곱수

    for digit in reversed(bin_str):
        if digit == '1':
            decimal_number += 2**power
        power += 1

    return decimal_number

hex_string = input()
binary_string = hex_bin(hex_string)

for i in range(0, len(binary_string), 7):
    print(bin_dec(binary_string[i:i+7]), end=' ')