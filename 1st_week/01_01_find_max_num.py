# def find_max_num(array):
#     for number in array:
#         is_max_num = True
#         for compare_number in array:
#             if number < compare_number:
#                 is_max_num = False
#         if is_max_num:
#             return number

def find_max_num(array):
    max_num = array[0]

    for number in array:
        if max_num < number:
            max_num = number
    return max_num

# 1) 2*N^2+N
# 2) 2*N+1
# N과 N^2은 N이 커질수록 큰 차이가 난다.
# N의 지수를 먼저 비교하면 시간복잡도 차이가 쉽게 구분된다.
# 매번 코드로 N이 아닌 연산 횟수를 전부 구하는 것은 불가능하다. (상수를 제외하고 표현하면 된다.)
# 1) N^2+N
# 2) N
# 3) N과 상관 없는 상수 연산량이 필요한 경우 1만큼의 시간복잡도가 있다라고 표현

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))