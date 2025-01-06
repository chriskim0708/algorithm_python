# ascii code
# 컴퓨터는 오로지 숫자 밖에 저장할 수 없다.
# 문자를 나타내기로 약속한 숫자 코드를 바로 ASCII 코드라고 한다.

# 문자를 ascii code로 변환
print(ord('a'))
# ascii code를 문자로 변환
print(chr(97))

# d -> index 3
# ord('d')의 ascii 코드에서 ord('a')의 ascii 코드를 빼면
# index 추출 가능
# ord('d') - ord('a')
index = ord('d') - ord('a')
print(index)