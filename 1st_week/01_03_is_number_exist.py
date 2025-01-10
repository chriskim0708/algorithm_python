def is_number_exist(number, array):
    for element in array:
        if element == number:
            return True
    return False

result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3,[3,5,6,1,2,4])) # 최선의 경우 시간복잡도는 1 (빅오메가 표기법)
print("정답 = Flase 현재 풀이 값 =", result(7,[6,6,6])) # 최악의 경우 시간복잡도는 N (빅오 표기법)
print("정답 = True 현재 풀이 값 =", result(2,[6,9,2,7,1888]))

# 알고리즘은 대부분 빅오 표기법을 사용한다.
# 언제나 최악의 경우를 대비해야한다.
# 공간복잡도보다는 시간복잡도를 개선하기 위해 더 고민한다.