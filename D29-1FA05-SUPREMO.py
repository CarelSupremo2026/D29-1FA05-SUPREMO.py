import math

# Ask user to enter the coordinates of two points.
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the distance between them using the Euclidean distance formula.
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Display the result.
print(f"The distance between the two points is: {distance:.2f}")

# The math library is more practical than writing all calculations from scratch because it saves time and reduces complex coding.
# Using ready-to-use functions in the math library such as sqrt() and pow() simplified the equation for the distance.
# Without the math library, calculating a square root would make the program longer, hard to read and have coding problems.
# The distance formula helps the user find the distance between two points on a coordinate plane.