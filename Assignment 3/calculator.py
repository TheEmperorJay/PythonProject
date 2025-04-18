import  math
n = int(input("Enter the first number: "))
def mathmodule(n):
    sqrt = math.sqrt(n)
    logarithm = math.log(n)
    sin = math.sin(n)
    print("Square root of number is:",sqrt)
    print("Natural Logarithmic value of number is:", logarithm)
    print("Sine value of the number is:",sin)
mathmodule(n)