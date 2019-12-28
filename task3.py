some_list = list(input("Введите элементы: ").split())
step_ = int(input("Введите шаг сдвига: "))
if step_ < 0:
    step_ = step_ * (-1)
    for item in range(step_):
        x = some_list.pop(0)
        some_list.append(x)
else:
    for item in range(step_):
        y = some_list.pop()
        some_list.insert(0, y)
print(some_list)
