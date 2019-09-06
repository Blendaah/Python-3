def prime_number_check(number):
    if number > 1:
        
        for i in range(2, number):
            if (number / i).is_integer():
                return False
        return True
    else:
        return False

print (prime_number_check(91))
