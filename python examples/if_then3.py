#scaline triangle: all sides have different lengths
#isosceles triangle: two sides have the same length
#equilateral triangle: all sides are equal

a=int(input("The length of side a= "))
b=int(input("The length of side b= "))
c=int(input("The length of side c= "))

if a!=b and b!=c and a!=c:
	print("This is a scalene triangle.")
elif a==b and b==c:
	print("This is an equilateral triangle.")
else:
	print("This is an isosceles triangle.")	