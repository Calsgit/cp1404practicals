"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When either of the inputs cannot be converted to an integer
2. When will a ZeroDivisionError occur?
When the denominator is set to zero, which is impossible to divide by
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Adding an extra validity check to the denominator to ensure it is not equal to zero
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")
