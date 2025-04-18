n = int(input("Enter the number to find factorial: "))

def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))
result = factorial(n)
print("The factorial of number is:",result)