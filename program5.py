# Exchange values of two variables
a, b = 5, 10
a, b = b, a

# Circulate values of n variables
def circulate(lst):
    return lst[1:] + lst[:1]

# Distance between two points
import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Example usage
print(a, b)  # Output: 10 5
print(circulate([1, 2, 3]))  # Output: [2, 3, 1]
print(distance(1, 2, 4, 6))  # Output: 5.0
