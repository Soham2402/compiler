operators = ['+', '-', '*', '/', '(', ')']
precedance = {'+':1, '-':1, '*':2, '/':2}


def infix_postfix(exp):
    stack = []
    postfix = ""
    
    for i in exp:
#         print(f"stack = {stack} output {postfix}")
        if i not in operators:
            postfix+=i
        
        elif i == "(":
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
        
        else:
            while stack and stack[-1] != '(' and precedance[stack[-1]] >= precedance[i]:
                postfix+=stack.pop()
            stack.append(i)
            
                
    while stack:
        x=stack.pop()
        if x != '(' or x!=')':
            postfix+=x
    
    return postfix
                
infix_postfix('A+B/C*(D-A)')