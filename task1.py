text_from_user = input("Введите текст: ")
up_case = 0
low_case = 0
for i in text_from_user:
    if i.isupper():
        up_case += 1
    elif i.islower():
        low_case +=1
summ = up_case + low_case
x = (up_case * 100) / summ
y = (low_case * 100) / summ
print(f"В введенном тексте {round(x, 2)}% заглавных и {round(y, 2)}% строчных букв")