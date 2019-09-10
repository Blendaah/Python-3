def delete_string(array, string):
    if string in array:
        array.remove(string)
        return array
    else:
        return False

print (delete_string(["a", "b", "c", "d", "e"], "c"))
