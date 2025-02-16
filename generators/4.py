def squares(a, b):
    for i in range (a, b+1):
        yield i**2
a= int(input("enter the value of a: "))
b= int(input("enter the value of b: "))
for num in squares(a,b):
    print(num)