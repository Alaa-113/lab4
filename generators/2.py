def even_numbers(n):
    for i in range(0, n, 2):
        yield i

n = int(input("Enter the value of n: "))

even= even_numbers(n)
print(', '.join(map(str, even)))