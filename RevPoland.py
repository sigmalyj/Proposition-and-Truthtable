def precedence(op):
    """返回运算符的优先级"""
    if op == '!':
        return 4
    elif op == '&':
        return 3
    elif op == '|':
        return 2
    elif op == '^':
        return 1
    elif op == '~':
        return 0
    return -1

def infix_to_postfix(formula):
    """将中缀表达式转换为后缀表达式"""
    stack = []  # 运算符堆栈
    postfix = []  # 后缀表达式
    tokens = formula.split()

    for token in tokens:
        if token.isalnum():  # 如果是变量或常数，直接添加到后缀表达式
            postfix.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # 移除'('
        else:  # 运算符
            while stack and precedence(token) <= precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(token)

    # 将剩余的运算符添加到后缀表达式
    while stack:
        postfix.append(stack.pop())

    return ' '.join(postfix)

# # 示例
# infix_formula = "( a & b ) | ( c ^ d )"
# postfix_formula = infix_to_postfix(infix_formula)
# print("后缀表达式:", postfix_formula)
