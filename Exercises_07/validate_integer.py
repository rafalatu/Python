from re import A

def validate_integer():
    # Loop forever
    while True:
        try:
            user_input = int(input("Enter an integer value: "))
        except:
            # Bad value, 
            print("Error")
            continue
        else:
            print("Valid input")
            # Good value, exit the loop
            break
        finally:
            # Continue
            print("This message shows every time, regardless of the programme flow")
    

validate_integer()

def calculate_endurance(fuel, fuel_consumption):
    try:
        if fuel_consumption == 0:
            raise ZeroDivisionError("Fuel consumption rate cannot be zero.")
        endurance = fuel / fuel_consumption
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except ValueError:
        return "Error: Invalid input. Please enter valid numerical values for fuel and fuel consumption."
    else:
        return endurance

# Example usage:
fuel = input("Enter fuel in liters: ")
fuel_consumption = input("Enter fuel consumption rate in liters per minute: ")

try:
    fuel = float(fuel)
    fuel_consumption = float(fuel_consumption)
    result = calculate_endurance(fuel, fuel_consumption)
    print(f"Remaining endurance: {result} minutes")
except ValueError:
    print("Error: Invalid input. Please enter valid numerical values for fuel and fuel consumption.")

    # Raising Exceptions
    # Take an input number as a string and convert it to an integer
my_value = int(input("Enter an integer greater than 0"))

if my_value <= 0:
    raise Exception("Values must be > 0")
else:
    print("Validation checks passed")
