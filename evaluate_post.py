operators = ['+', '-', '*', '/', '(', ')']
precedance = {'+':1, '-':1, '*':2, '/':2}


def eval_postfix(exp):
    exp = exp.split()
    stack = []
    
    for i in exp:
        if i not in operators:
            stack.append(int(i))
        elif i == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif i == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif i == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif i == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)
            
    return stack
eval_postfix("10 5 3 - / 2 6 * +")