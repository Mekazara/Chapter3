def isBalanced(s):
    opening_bracket = ["(", "[", "{"]
    closing_bracket = [")", "]", "}"]
    ls = []
    for item in s:
        if item in opening_bracket:
            ls.append(opening_bracket.index(item))
        elif item in closing_bracket and len(ls) != 0:
            if ls[-1] == closing_bracket.index(item):
                ls.pop()
            else:
                ls.append(item)
        elif item in closing_bracket:
            ls.append(item)
    if ls:
        return "NO"
    else:
        return "YES"
print(isBalanced("{(([])[])[]]}"))
print(isBalanced("{[}"))
print(isBalanced("}([[{)[]))]{){}["))
print(isBalanced("{]]{()}{])"))
print(isBalanced("(){}"))
print(isBalanced("{}{()}{{}}"))