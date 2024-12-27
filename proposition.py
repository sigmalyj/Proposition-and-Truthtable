import itertools
import re
from RevPoland import *

# 定义逻辑运算符的映射
operator_map = {
    '!': lambda x: not x,
    '&': lambda x, y: x and y,
    '|': lambda x, y: x or y,
    '^': lambda x, y: not x or y,
    '~': lambda x, y: x == y
}

# 检查公式语法
def check_syntax(formula):
    # 确保公式只包含逻辑运算符、括号和命题变量
    if not re.match(r'^[!&|^~()a-zA-Z ]*$', formula):
        return False
    # 确保括号匹配
    if formula.count('(') != formula.count(')'):
        return False
    return True

# 解析后缀表达式并计算结果
def evaluate_formula(formula, assignment):
    stack = []
    for token in formula.split():
        if token in operator_map:
            if token == '!':
                if len(stack) < 1:
                    raise ValueError("公式错误：缺少操作数")
                arg = stack.pop()
                stack.append(operator_map[token](arg))
            else:
                if len(stack) < 2:
                    raise ValueError("公式错误：缺少操作数")
                arg2 = stack.pop()
                arg1 = stack.pop()
                stack.append(operator_map[token](arg1, arg2))
        elif token.isalpha():
            stack.append(assignment[token])
        else:
            raise ValueError(f"未知的符号：{token}")
    if len(stack) != 1:
        raise ValueError("公式错误：操作数和运算符不匹配")
    return stack[0]

# 生成真值表
def generate_truth_table(infix_formula, postfix_formula):
    # 提取命题变量
    variables = sorted(set(re.findall(r'[a-zA-Z]', postfix_formula)), key=lambda x: ord(x))
    
    # 生成所有可能的真值组合
    truth_values = list(itertools.product([False, True], repeat=len(variables)))
    
    # 打印表头
    print(' | '.join(variables + [infix_formula]))
    
    # 计算并打印每一行的真值
    for values in truth_values:
        # 创建一个字典，将变量名映射到其对应的真值
        assignment = dict(zip(variables, values))
        # 计算公式的真值
        result = evaluate_formula(postfix_formula, assignment)
        # 打印结果
        print(' | '.join(['T' if v else 'F' for v in values] + ['T' if result else 'F']))
