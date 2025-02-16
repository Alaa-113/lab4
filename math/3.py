import math 
sides=int(input("enetr the number of sides"))
length=float(input("enter the length of the sides"))
area=float((sides*length**2)/(4*math.tan(math.pi/sides)))
print(f"the area is {area:.2f}")