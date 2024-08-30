#find the common elements between two lists
def common_elements():
    l1 = [1,2,3,4,5]
    l2 = [4,5,6]
    lst_1 = set(l1)
    lst_2 = set(l2)
    unique_ele = lst_1.intersection(lst_2)
    print(unique_ele)


common_elements()