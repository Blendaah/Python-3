def del_key(dictionary, key):
    del dictionary[key]
    return dictionary

print (del_key({"aaa":1, "bbb":2, "ccc":3}, "bbb"))
