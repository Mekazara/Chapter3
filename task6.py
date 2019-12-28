def isBalanced(s):
    ls = []
    opening_bracket = ["(", "[", "{"]
    closing_bracket = [")", "]", "}"]
    for item in s:
        if item in opening_bracket:
            ls.append(opening_bracket.index(item))
        elif item in closing_bracket:
            if len(ls) == 0:
                return "NO"
            if ls[-1] == closing_bracket.index(item):
                ls.pop()
            else:
                return "NO"
    return "YES"

print(isBalanced("{}"))
print(isBalanced("}([[{)[]))]{){}["))
print(isBalanced("{]]{()}{])"))
print(isBalanced("(){}"))
print(isBalanced("{}{()}{{}}"))
