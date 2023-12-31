my_list = []
my_string = "Morning Folks!"
for letter in my_string:
    my_list.append(letter)

print(my_list)

my_list = [number for number in range(0,20)]
print(my_list)

my_list = [number * 10 for number in range(0,20) if number < 10]
print(my_list)

conversion = 0.3048
my_depth_in_feet = [12.3, 13.8, 15.3, 12.1, 8.8]
my_depth_in_meters = [(round(depth * conversion, 2)) for depth in my_depth_in_feet] 
print(my_depth_in_meters)


# Createing a list of 10 temperature values in Kelvin
kelvin_temperatures = [220, 410, 620, 230, 140, 750, 460, 770, 777, 677]

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Iterate through the list and convert/print in both Celsius and Fahrenheit
for kelvin in kelvin_temperatures:
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = kelvin_to_fahrenheit(kelvin)
    print(f"{kelvin} K is {celsius:.2f} °C and {fahrenheit:.2f} °F")
