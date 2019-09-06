def highest_of_3(numbers):
    if numbers[0] > numbers[2] and numbers[0] > numbers[1]:
        return numbers[0]
            
    elif numbers[1] > numbers[0] and numbers[1] > numbers[2]:
        return numbers[1]
        
    elif numbers[2] > numbers[0] and numbers[2] > numbers[1]:
        return number[2]
            

print (highest_of_3([6, 1, 6]))
