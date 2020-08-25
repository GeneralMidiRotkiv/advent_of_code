password_range_start = 264360
password_range_end = 746325

#Make a list with all the numbers from start to end of the password range
def make_number_list(start, end):
    consecutive_numbers = set()
    for i in range(start, end):
        consecutive_numbers.add(str(i))
    return consecutive_numbers

consecutive_numbers = make_number_list(password_range_start, password_range_end)

print("Full length:", len(consecutive_numbers))

def remove_decreasing_numbers(list):
    new_set = list.copy()
    for str_number in list:
        for i in range(5):
            if int(str_number[i]) > int(str_number[i+1]):
                new_set.remove(str_number)
                break
    return new_set

cleaned_numbers = remove_decreasing_numbers(consecutive_numbers)
print("Length after Step 1:", len(cleaned_numbers))
#print(cleaned_numbers)

def remove_without_doubles(set):
    new_set = {0}
    for str_number in set:
        for i in range(1,10):
            if str(i*11) in str_number:
                #print(i*11, "in", str_number)
                new_set.add(str_number)
    new_set.remove(0) 
    return new_set

cleaned_numbers = remove_without_doubles(cleaned_numbers)   
print("Length after Step 2:", len(cleaned_numbers))