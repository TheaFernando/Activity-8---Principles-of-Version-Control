# ===================================================================================================
# AUTHOR: Thea Margaux M. Fernando
# SECTION: 8 - Sampaguita
# Activity 2: Distance Formula
# ===================================================================================================

# This library is to define the undefined terms such as math.sqrt() and math.pow()
import math

print("First point")
x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
print("Second Point")
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))

distance = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))

print(f"\nThe distance between the two points is: {distance: .2f}")

# Reflection
# The math library helped me simplify my program because instead of typing the distance formula manually,
# I can use the built-in functions, sqrt() and pow(). Because of the library, it also made using sqrt()
# and pow() easier to use since without these functions, my programs would be much harder and longer to make
# due to the exponents and square roots I need to type manually.