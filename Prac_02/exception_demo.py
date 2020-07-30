"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
 when user enter a, b ,c into the program
2. When will a ZeroDivisionError occur?
if user give a zero input, then ZeroDivisionError will occur.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
valid_numerator = False
valid_denominator = False
while valid_numerator == False or valid_denominator == False:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        valid_denominator = True
        valid_numerator = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")