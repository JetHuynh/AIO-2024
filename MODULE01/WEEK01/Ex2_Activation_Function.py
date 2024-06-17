"""## 2. Viết function mô phỏng theo 3 activation function."""
import math

# calculate  sigmoid Function


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# calculate Rectified Linear Unit Function


def relu(x):
    return max(0, x)

# calculate Exponential Linear Unit Function


def elu(x, alpha=1.0):
    return alpha * (math.exp(x) - 1) if x < 0 else x

# validate parameter


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# ctivation process


def activation_function():
    print('Activation Function')
    x = input('Input x = ')
    if not is_number(x):
        print("X parameter must be a number")
        return None
    else:
        x = float(x)

    activation_function = input(
        'Input activation function (sigmoid | relu | elu): ')
    if activation_function == 'sigmoid':
        result = sigmoid(x)
    elif activation_function == 'relu':
        result = relu(x)
    elif activation_function == 'elu':
        result = elu(x)
    else:
        print(f'{activation_function} is not supported')
        return None

    print(f'{activation_function}: f({x}) = {result}')


# RunExample
activation_function()
