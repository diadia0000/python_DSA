def uniqueLetterString(string):
    right = 0
    left = 0
    stringLength = 0
    sub_string = ""
    while right < len(string):
        if string[right] not in sub_string:
            sub_string += string[right]
            right+=1
        else:
            sub_string = ""
            stringLength = max(stringLength, right-left)
            left = right
    return max(stringLength, right-left)
print(uniqueLetterString("thisishofwedoit"))
