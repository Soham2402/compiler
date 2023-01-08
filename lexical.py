def lexical_analysis(code):
    # Create a list of tokens
    tokens = []
    
    # Split the code into lines
    lines = code.split()
    print(lines)
    # Iterate through each line of code
    for word in lines:
                
        # Check if the word is a keyword
        if word in ["int", "float", "double", "char", "void", "for", "while", "if", "else"]:
            tokens.append(("keyword", word))
            continue
                
            # Check if the word is an operator
        if word in ["+", "-", "*", "/", "=", "==", "!=", ">", "<", ">=", "<="]:
            tokens.append(("operator", word))
            continue
                
            # Check if the word is a punctuation mark
        if word in [";", ",", "{", "}"]:
            tokens.append(("punctuation", word))
            continue

                
            # If the word is none of the above, it is considered a identifier
        tokens.append(("identifier", word))
            
    return tokens

# Test the lexical analysis function
code = """
int main() {
  int x = 5;
  int y = 6;
  int z = x + y;
  return 0;
}
"""

lexical_analysis(code)