def list_add(mylist, e):
    if e is None:
        raise ValueError 
    new_list = mylist
    new_list.append(e)
    return new_list

print(list_add([5, 2, 4], 2))