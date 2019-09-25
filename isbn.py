"""
Tung Hoang - 09/25/19
This program checks if the ISBN number that the user input is valid or not.
It does so by checking the sum of the digits multiply by their placement and
sees if it is divisible by 11
"""

# Initialize the sum 
sum = 0

# Asking user for ISBN input and checks if it is a valid 10 digit number.
isbn = input("Number: ")

while isbn.isdigit() == False or len(isbn) != 10:
    isbn = input("Retry: ")

isbn = int(isbn)

# Loop through the digit starting from the 10th place and multiply it by
# their placement to find the sum.
for i in range(10, 0, -1):
    sum = sum + (isbn % 10 * i)
    isbn = isbn // 10

# Checking if that 10 digit number is an ISBN or not.
if sum % 11 == 0:
    print("YES")
else:
    print("NO")
