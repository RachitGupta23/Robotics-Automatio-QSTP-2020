import math

def polar(x, y):
	mag = (x**2 + y**2)**0.5
	ang = math.atan(y/x)
	print("Polar Coordinates are (" + str(mag) + "," + str(ang) + ") \n")

def cartesian(mag, angle):
	x = mag * math.cos(angle)
	y = mag * math.sin(angle)
	print("Cartesian Coordinates are (" + str(x) + "," + str(y) + ") \n")

option = int(input("""1) Cartesian to Polar \n 2) Polar to Cartesian
	\n Enter choice (1 or 2)"""))
if option == 1:
	x = float(input("Enter X - Coordinate \n"))
	y = float(input("Enter Y - Coordinate \n"))
	polar(x,y)
elif option == 2:
	mag = float(input("Enter modulus of Coordinate \n"))
	ang = float(input("Enter Angle of coordinate in radians \n"))
	cartesian(mag, ang)
else:
	print ("Wrong option!")