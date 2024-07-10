def isSubsequence(str1,str2):
    if (len(str1) == 0 and len(str2)>0) or (len(str1) > 0 and len(str2) == 0):
        return "No"
    elif len(str1) == 0 and len(str2) == 0:return "Yes"
    i = 0 ; j = 0
    while j <len(str2):
        if str1[i] == str2[j]:
            i+=1
        if i >= len(str1):
            return "yes"
        j+=1
    return "No"
print(isSubsequence("hello","hello Dear"))
print(isSubsequence("book","brooklyn"))
print(isSubsequence("abc","bca"))
print(isSubsequence("abc","abc"))
print(isSubsequence("",""))
