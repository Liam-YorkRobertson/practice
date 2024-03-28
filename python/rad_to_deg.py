"""
Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians. The function should convert the radians into degrees and then return that value.
"""
from math import pi


def main():
    """
    changes radians to degrees
    """
    user_rad = int(input("Enter the radians you wish to have converted: "))
    print("You entered " + str(user_rad) + " radians.")
    degrees = (user_rad * 180 / pi)
    print(str(user_rad) + " radians is " + str(degrees) + " degrees")
    return


if __name__ == "__main__":
    main()
