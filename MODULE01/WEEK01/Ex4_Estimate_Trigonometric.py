"""## 4. Viết 4 functions để ước lượng các hàm số: sin(x), cos(x), sinh(x), cosh(x)"""
import math

# calc factorial


def factorial(n):
    if not isinstance(n, int) or n < 0:
        print("Sencond parameter must be an positive integer number")
        return None

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


warn = "First parameter must be a radian"
# estimate Sin(x) function


def est_sin(x, n):
    if not isinstance(x, float):
        print(warn)
        return None

    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return result

# estimate Cos(x) function


def est_cos(x, n):
    if not isinstance(x, float):
        print(warn)
        return None

    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    return result

# estimate Sinh(x) function


def est_sinh(x, n):
    if not isinstance(x, float):
        print(warn)
        return None

    result = 0
    for i in range(n):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return result

# estimate Cosh(x) function


def est_cosh(x, n):
    if not isinstance(x, float):
        print(warn)
        return None

    result = 0
    for i in range(n):
        result += (x ** (2 * i)) / factorial(2 * i)
    return result


# RunExample
print(est_sin(math.pi/2, 10))
print(est_cos(math.pi/2, 10))
print(est_sinh(math.pi, 10))
print(est_cosh(math.pi, 10))
