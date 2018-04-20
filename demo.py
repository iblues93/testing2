#declaring function
def get_average( list_of_numbers ): # the list_of_numbers is the list of numbers you want to figure out

    total = sum(list_of_numbers)
    length = len(list_of_numbers)
    average = total/length
    return average
