def is_anagram(string_1, string_2):
    if len(string_1) != len(string_2):
        return False

    cnt_array = [0 for _ in range(1500)]

    for char in string_1:
        cnt_array[ord(char)] += 1

    for char in string_2:
        cnt_array[ord(char)] -= 1
    for cnt in cnt_array:
        if cnt > 0:
            return False
    return True
