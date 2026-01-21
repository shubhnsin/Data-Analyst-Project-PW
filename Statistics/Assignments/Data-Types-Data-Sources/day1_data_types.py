# ------------------------------------------------------------
# Day 1: Understanding Data Types
# Task:
# 1. Accept different data types (integer, float, string, boolean)
# 2. Identify and display their data types using type()
# 3. Store the values in a dictionary with data type names as keys
# ------------------------------------------------------------

def analyze_inputs():
    """
    This function accepts different types of input values,
    identifies their data types, and stores them in a dictionary.
    """

    print("----- Day 1: Data Type Analyzer -----\n")

    # Dictionary to store values with their data type names as keys
    type_storage = {}

    # Taking inputs from the user
    integer_value = int(input("Enter an integer value: "))
    float_value = float(input("Enter a float value: "))
    string_value = input("Enter a string value: ")
    boolean_value = input("Enter True or False: ") == "True"

    # Storing all inputs in a list for easy iteration
    inputs = [integer_value, float_value, string_value, boolean_value]

    # Display header for output
    print(f"\n{'Input Value':<20} | {'Data Type':<20}")
    print("-" * 45)

    # Loop through each input value
    for item in inputs:
        # Identify the data type of the value
        data_type = type(item)
        data_type_name = data_type.__name__

        # Print value and its data type
        print(f"{str(item):<20} | {data_type_name:<20}")

        # Store value in dictionary with data type as key
        type_storage[data_type_name] = item

    # Display the final dictionary
    print("\nStored Dictionary:")
    print(type_storage)


# This condition ensures the function runs
# only when this file is executed directly
if __name__ == "__main__":
    analyze_inputs()
