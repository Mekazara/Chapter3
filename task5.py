def twoStrings():
    p = int(input("Enter the number of test cases: "))
    for i in range(p):
        s1 = input("Print any word: ").lower()
        s2 = input("Print any word: ").lower()
    for i in range(p):
        count = 0
        for letter in s1:
            if letter in s2:
                count += 1
            else:
                continue
        if count >= 1:
            answer = "YES"
        else:
            answer = "NO"
        print(answer)
twoStrings()

# for hackerrank
# count = 0
# answer = None
# for letter in s1:
#     if letter in s2:
#         answer = "YES"
#         count += 1
#     else:
#         answer = "NO"
# if count >= 1:
#     return "YES"
# else:
#     return "NO"
# print(answer)
