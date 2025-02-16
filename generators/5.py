def numbers(n):
    for i in range (n,-1,-1):
        yield i
n= int(input("enter the value of n "))
for num in numbers(n):
    print(num)