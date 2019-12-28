def find_min_num(some_list):
    another_list = []
    for item in range(min(some_list) + 1, max(some_list)):
        another_list.append(item)
        if min(another_list) in some_list:
            another_list.remove(min(another_list))
        elif min(another_list) not in some_list:
            a = (min(another_list))
    print(some_list)
    print(a)
    print()
find_min_num([1, 2, 4, 5, 7, 10])
find_min_num([11, 15, 17, 38, 24, 66])
find_min_num([56, 34, 12, 78])