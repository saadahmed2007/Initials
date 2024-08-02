num1 = input ("Enter any number: ") # taking input of a number as string
num2 = input("Enter another number: ") # taking input of a number as string

num1 = int(num1)
num2 = int(num2)

# starting addition 
result = num1 + num2

print(f"Sum of {num1} and {num2} is {result}")

# starting multiplication
result2 = num1 * num2

print(f"Multiple of {num1} and {num2} is {result2}")


# starting subtraction
result3 = num1 - num2
print(f"Difference between {num1} and {num2} is {result3}")





# starting division
if num2 != 0:
    result4 = num1 / num2
    print(f"Division of {num1} by {num2} is {result4}")
else:
    print("Error: Division by zero is not allowed.")
    