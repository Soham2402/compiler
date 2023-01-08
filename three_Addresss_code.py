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
    print(postfix)
    return postfix


def generate3AC(exp):
    stack = []
    t = 1
    tac = []
    for i in exp:
        if i not in operators:
            stack.append(i)
        else:
            print(f't{t} = {stack[-2]} {i} {stack[-1]}')
            tac.append([f't{t} = {stack[-2]} {i} {stack[-1]}'])
            stack = stack[:-2]
            stack.append(f"t{t}")
            t += 1
    return tac
def main():
    exp = input("enter expression without spac: ")
    pos = infix_postfix(exp)
    print(generate3AC(pos))
    
main()