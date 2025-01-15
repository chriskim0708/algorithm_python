input = "abadabac"

def find_not_repeating_first_character(string):
    start_index = ord('a')
    repeat_alphabet_array = [0] * 26

    for alphabet in string:
        if not alphabet.isalpha():
            continue
        alphabet_index = ord(alphabet) - start_index
        repeat_alphabet_array[alphabet_index] += 1

    no_repeat_alphabet_array = []

    for i, value in enumerate(repeat_alphabet_array):
        if value == 1:
            no_repeat_alphabet_array.append(chr(i + start_index))

    for char in string:
        if char in no_repeat_alphabet_array:
            return char

    return '_'


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaaa"))