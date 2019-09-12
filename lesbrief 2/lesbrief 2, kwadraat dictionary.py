def create_dict(number):
    dictionary = {}

    for i in range(number):
        dictionary[i + 1] = (i+1) * (i+1)
    print (dictionary)

create_dict(5)
