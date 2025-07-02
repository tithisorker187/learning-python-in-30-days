#problem-1
#Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

x1=int(input("enter x1"))
x2=int(input("enter x2"))
y1=int(input("enter y1"))
y2=int(input("enter y2"))
distance= (((x2-x1)**2+(y2-y1)**2))**0.5
print(distance)


#problem-2
### Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.
input1=input("enter first number")
input2=input("enter second number")


### Q4:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

# Get input from user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the result
print(f"Simple Interest = {simple_interest}")

#Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
#For example: Input: heads -> 4 legs -> 12
Output: dogs -> 2 chicken -> 2




heads = int(input("Enter total number of heads: "))
legs = int(input("Enter total number of legs: "))

# Solve using simple math
# Let c = number of chickens, d = number of dogs
# c + d = heads
# 2c + 4d = legs

# Try all possible values of dogs (d) from 0 to heads
found = False
for dogs in range(heads + 1):
    chickens = heads - dogs
    total_legs = 2 * chickens + 4 * dogs
    if total_legs == legs:
        print(f"Number of chickens: {chickens}")
        print(f"Number of dogs: {dogs}")
        found = True
        break

if not found:
    print("No valid solution exists with the given heads and legs.")






