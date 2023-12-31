def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            pass

result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)

# 1. Why do you get the value None?
# When a Python function doesn't have a return statement or the execution path doesn't reach a return statement, it returns None by default.
# 2. What values in the final statement will result in the function returning True? Why?
# In the provided code, there are no values that will result in the function returning True because it doesn't have a return True statement inside the loop
# 3. Can you modify this function to return False instead of None if the value is not found?
# Yes, you can modify the function to explicitly return False when the loop completes without finding the value