def addup_dictionary(dictionary):
    total = 0
    for key, value in dictionary.items():
        total += value
    return total

print (addup_dictionary({1:2,2:6,3:5}))
