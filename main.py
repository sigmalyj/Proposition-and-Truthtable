from proposition import *
from truth_table import *
from paradigm import *

if __name__ == '__main__':
    mode = input("请选择功能（1. 生成真值表 2. 生成命题公式 3. 计算主析取范式和主合取范式）：")
    if mode == '1':
        infix_formula = input("请输入命题公式（使用a-zA-Z表示命题变量，!代表NOT，&代表AND，|代表OR，^代表IMPLIES，~代表EQUIVALENT，变量与运算符之间用空格分开）：")
        if check_syntax(infix_formula):
            try:
                postfix_formula = infix_to_postfix(infix_formula)
                generate_truth_table(infix_formula, postfix_formula)
            except ValueError as e:
                print(e)
        else:
            print("公式语法错误！")
    elif mode == '2':
        truthtable = input_truthtable()
        formula = generate_formula_from_truthtable(truthtable)
        print("生成的命题公式:", formula)
    elif mode == '3':
        formula = input("请输入命题公式（使用a-zA-Z表示命题变量，!代表NOT，&代表AND，|代表OR，^代表IMPLIES，~代表EQUIVALENT）：")
        show_cnf_dnf(formula)
    else:
        print("无效的选项！")