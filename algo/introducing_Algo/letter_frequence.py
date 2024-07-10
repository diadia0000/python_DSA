def sameFrequency(str1, str2):
    if len(str1) != len(str2):
        return "false"
    letter_1 = {}
    letter_2 = {}
    for letter in str1:
        if letter not in letter_1:
            letter_1[letter] = 1
        else:
            letter_1[letter] += 1
    for letter2 in str2:
        if letter2 not in letter_2:
            letter_2[letter2] = 1
        else:
            letter_2[letter2] += 1
    if letter_1 == letter_2:
        return "true"
    return "false"


print(sameFrequency("hello", "hello"))
