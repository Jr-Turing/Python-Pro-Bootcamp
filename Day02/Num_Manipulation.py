# Number Manipulation and F Strings in Python 
print(int(8 / 3)) # Outputs 2 becasue it converts the float to an integer
print(round(8 / 3)) # Outputs 3 because it rounds the float to the nearest integer
print(round(8 / 3, 2)) # Outputs 2.67 because it rounds the float to 2 decimal places

# check the data type
print(type(4 / 2)) # Outputs <class 'float'>
# // is the floor-division operator that rounds down to the nearest whole number
print(type(4 // 2)) # Outputs <class 'int'>

# Examples
score = 0
height = 1.8
isWinning = True

# user scores a point
score += 1

# f-strings
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}") # Outputs Your score is 1