# Define the main function 
def main():
    # Initialize variables
    num1 = 1  # An integer variable with the value 1
    num2 = 2  # An integer variable with the value 2
    str_val = "JOR"  # A string variable with the value "JOR"

    # Perform arithmetic operations and concatenate strings, then print the results
    print(num1 + num2)  # Print the sum of num1 and num2
    print(num1 + num2)  # Print the sum of num1 and num2 (this line appears twice)
    print(str(num1) + str_val)  # Convert num1 to a string, concatenate with str_val, and print

# Check if the script is the main program entry point
if __name__ == "__main__":
    # Call the main function to start the program
    main()
