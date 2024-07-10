def is_palindrome_stack(txt):
    '''
     time O(2n)
     space O(n)
    '''
    stack = []
    palindrome = ""
    for i in txt:
        stack.append(i)
    while stack:
        palindrome += stack.pop()
    return palindrome == txt

def is_palindrome_pointer(txt):
    '''
     time O(n)
     space O(1)
    '''
    left = 0
    right = len(txt)-1
    while left<=right:
        if txt[left] != txt[right]:
            return 0
        left+=1
        right-=1
    return 1


Map = {0: "false", 1: "true"}
print(Map[is_palindrome_stack("awesome")])
print(Map[is_palindrome_stack("tacocat")])

print(Map[is_palindrome_pointer("awesome")])
print(Map[is_palindrome_pointer("tacocat")])