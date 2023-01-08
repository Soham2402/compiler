def machinecode(code):
    output = []
    for i in range(len(code)):
        ind_chars = code[i].split()
        
        if len(ind_chars) == 5:
            if ind_chars[3] == "+":
                output.append(f"LOAD {ind_chars[2]}")
                output.append(f"ADD {ind_chars[-1]}")
                output.append(f"STORE {ind_chars[0]}")
                
            if ind_chars[3] == "-":
                output.append(f"LOAD {ind_chars[2]}")
                output.append(f"SUB {ind_chars[-1]}")
                output.append(f"STORE {ind_chars[0]}")
                
            if ind_chars[3] == "/":
                output.append(f"LOAD {ind_chars[2]}")
                output.append(f"DIVIDE {ind_chars[-1]}")
                output.append(f"STORE {ind_chars[0]}")
                
            if ind_chars[3] == "*":
                output.append(f"LOAD {ind_chars[2]}")
                output.append(f"DIVIDE {ind_chars[-1]}")
                output.append(f"STORE {ind_chars[0]}")
            
        if len(ind_chars) == 3:
            output.append(f"LOAD {ind_chars[2]}")
            output.append(f"STORE {ind_chars[0]}")
            
    return output

print(machinecode(["t1 = a + b","t2 = c + d"]))