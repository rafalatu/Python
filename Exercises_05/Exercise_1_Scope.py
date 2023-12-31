def divisible(numerator: int, denominator: int)->bool:
    return numerator % denominator == 0

print(divisible(30,4))

# this code defines a function divisible that 
# checks if one number is evenly divisible by another, 
# and it returns True if the division has no remainder and 
# False otherwise. In this specific case, 
# it calls the function with 30 as the numerator and 4 as the 
# denominator, which results in False because 30 is not evenly 
# divisible by 4.