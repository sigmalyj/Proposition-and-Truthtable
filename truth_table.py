def generate_formula_from_truthtable(truthtable):
    variables = 'abcdefghijklmnopqrstuvwxyz'
    formula_parts = []

    for row in truthtable:
        if row[-1] == 1:  # 只考虑真值行的条件
            literals = []
            for i, val in enumerate(row[:-1]):
                if val == 0:
                    literals.append('!' + variables[i])
                else:
                    literals.append(variables[i])
            formula_parts.append('&'.join(literals))

    # 如果所有部分都是空的，则表示命题公式是永假式
    if not formula_parts:
        return '0'  # 永假式可以用0表示

    # 使用析取(|)将所有部分组合起来
    formula = '|'.join(formula_parts)
    return formula

# 从终端输入真值表
def input_truthtable():
    truthtable = []
    rows = int(input("请输入真值表的行数: "))
    cols = int(input("请输入真值表的列数: "))
    
    print("请输入真值表，每行输入一个真值行，用空格分隔每个值:")
    for _ in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            raise ValueError("输入的列数不匹配，请重新输入")
        truthtable.append(row)
    
    return truthtable

if __name__ == "__main__":
    truthtable = input_truthtable()
    formula = generate_formula_from_truthtable(truthtable)
    print("生成的命题公式:", formula)