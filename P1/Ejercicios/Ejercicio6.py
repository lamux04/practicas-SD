def list_del(mylist, e):
    new_list = mylist
    new_list.remove(e)
    return new_list

print(list_del([5, 2, 4], 2))