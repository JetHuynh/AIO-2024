"""## 4. Viết 4 functions để ước lượng các hàm số: sin(x), cos(x), sinh(x), cosh(x)"""
import math

# calc factorial
def Factorial(n):
    if not isinstance(n, int) or n < 0 :
        print("Sencond parameter must be an positive integer number")
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# estimate Sin(x) function
def est_Sin(x,n):
    if not isinstance(x, float):
        print("First parameter must be a radian")
        return None

    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / Factorial(2 * i + 1)
    return result

# estimate Cos(x) function
def est_Cos(x,n):
    if not isinstance(x, float):
        print("First parameter must be a radian")
        return None

    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i)) / Factorial(2 * i)
    return result

# estimate Sinh(x) function
def est_Sinh(x,n):
    if not isinstance(x, float):
        print("First parameter must be a radian")
        return None

    result = 0
    for i in range(n):
        result += (x ** (2 * i + 1)) / Factorial(2 * i + 1)
    return result

# estimate Cosh(x) function
def est_Cosh(x,n):
    if not isinstance(x, float):
        print("First parameter must be a radian")
        return None

    result = 0
    for i in range(n):
        result += (x ** (2 * i)) / Factorial(2 * i)
    return result

# RunExample
print(est_Sin(math.pi/2, 10))
print(est_Cos(math.pi/2, 10))
print(est_Sinh(math.pi, 10))
print(est_Cosh(math.pi, 10))