def square_numbers(n):
    for i in range(1, n+1):
     yield i**2 #yield produces a value and then pauses the function until the next value is requested, which makes it a generator.
n=int(input("enter the value of n"))
for square in square_numbers(n):
    print(square)


    