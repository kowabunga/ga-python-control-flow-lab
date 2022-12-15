# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a:
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

triangle_sides = []

for val in range(0, 3):
    triangle_sides.append(int(input("Enter one side of a triangle. > ")))

if triangle_sides[0] == triangle_sides[1] and triangle_sides[1] == triangle_sides[2]:
    print(
        f"A triangle with sides of {triangle_sides[0]}, {triangle_sides[1] }, {triangle_sides[2] }, is an equalateral triangle"
    )
elif triangle_sides[0] != triangle_sides[1] and triangle_sides[1] != triangle_sides[2]:
    print(
        f"A triangle with sides of {triangle_sides[0]}, {triangle_sides[1] }, {triangle_sides[2] }, is a scalene triangle"
    )
else:
    print(
        f"A triangle with sides of {triangle_sides[0]}, {triangle_sides[1] }, {triangle_sides[2] }, is an isosceles triangle"
    )
