def isBalanced(s):
    ls = []
    opening_bracket = ["(", "[", "{"]
    closing_bracket = [")", "]", "}"]
    for item in s:
        if item in opening_bracket:
            ls.append(item)
        elif item in closing_bracket:
            a = opening_bracket.index(ls[-1])
            if a == closing_bracket.index(item):
                ls.pop()
            else:
                return "NO"
    return "YES"

print(isBalanced("{[()]}"))
print(isBalanced("{[(])}"))
print(isBalanced("([[)"))
print(isBalanced("[](){()}"))
print(isBalanced("{)[](}]}]}))}(())("))
