# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/11/24
# Gets the user input for the base and height then
# Calculates the area of a triangle. Has the user input
# In the main() function and uses arguments and parameters
# to pass the values
# onto the calculate_area() function.


def calculate_area(base, height):

    # Calculating the area
    area = base * height / 2

    # Displaying the area back to the user
    print("The area of this triangle is {:.3}cm^2!".format(area))


# Getting the user input and calling calculate_area()
def main():
    # Title
    print("The Area of a Triangle\n")

    # Getting the user input for the base and height
    base_input_string = input("Enter the base of your triangle (cm): ")
    height_input_string = input("Enter the height of your triangle (cm): ")

    # Using Try Catch to make sure it is a string
    try:
        base_user_input = float(base_input_string)
        height_user_input = float(height_input_string)
    except Exception:
        print("Please enter a number!")
    else:
        if base_user_input <= 0:
            print("Please enter a positive number!")
        elif height_user_input <= 0:
            print("Please enter a positive number!")
        else:
            # Calling the function calculate_area()
            calculate_area(base_user_input, height_user_input)


if __name__ == "__main__":
    main()
