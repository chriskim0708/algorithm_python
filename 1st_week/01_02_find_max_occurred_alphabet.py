# alphabet 총 길이 26

def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    max_occurrence = 0
    max_occurrence_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0

        for char in string:
            if not char.isalpha():
                continue

            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_occurrence_alphabet = alphabet

    return max_occurrence_alphabet


# def find_max_occurred_alphabet(string):
#     start_index = ord('a')
#     max_occurred_count = 0
#     max_occurred_index = 0
#     occurred_list = [0] * 26
#
#     for text in string:
#         if not text.isalpha():
#             continue
#         index = ord(text) - start_index
#         occurred_list[index] += 1
#
#     for index, occurred_num in enumerate(occurred_list):
#         if occurred_num > max_occurred_count:
#             max_occurred_count = occurred_num
#             max_occurred_index = index
#
#     max_occurred_str = chr(start_index + max_occurred_index)
#
#     return max_occurred_str

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))
