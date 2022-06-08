def multiply_list_map(my_list=[], number=0):
    mnew_list = my_list.copy()
    return list(map(lambda x : (x * number) , my_list))
