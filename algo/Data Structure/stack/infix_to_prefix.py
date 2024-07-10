def is_operator(char):
    return char in ['+', '-', '*', '/', '^']


def precedence(op):
    if op == '^':
        return 3
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1
    return 0


def infix_to_prefix(expression):
    stack = []
    prefix = []
    for char in reversed(expression):
        if char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix.append(stack.pop())
            stack.pop()
        elif is_operator(char):
            while stack and precedence(stack[-1]) > precedence(char):
                prefix.append(stack.pop())
            stack.append(char)
        else:
            prefix.append(char)
    while stack:
        prefix.append(stack.pop())
    return ''.join(reversed(prefix))


# 測試程式碼
while True:
    try:
        infix_expression = input("請輸入中序表達式：")
        prefix_expression = infix_to_prefix(infix_expression)
        print("前序表達式：", prefix_expression)
    except EOFError:
        break
