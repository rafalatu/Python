def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            pass

result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)


def contains_even_number(number_list):
    for number in number_list:
        if number % 2 == 0:
            return True
    return False

calculate_cylinder_volume = lambda radius, height: 3.14159 * radius**2 * height

radius = 5
height = 10
volume = calculate_cylinder_volume(radius, height)
print(volume)

