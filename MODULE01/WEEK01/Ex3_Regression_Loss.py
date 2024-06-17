"""## 3. Viết function lựa chọn regression loss function để tính loss:"""
import math
import random
# Prepare_MAE Function


def pre_mae(y_target, y_pred):
    return abs(y_target - y_pred)

# Prepare_MSE Function


def pre_mse(y_target, y_pred):
    return (y_target - y_pred) ** 2


# Calculate regression loss function
def regression_loss_function():
    print('Regression Loss Function')
    # input&validate number of samples
    num_samples = input(
        'Input number of sampels (integer number) which are generated: ')
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return None
    else:
        num_samples = int(num_samples)
    # input&validate loss function
    loss_list = ['MAE', 'MSE', 'RMSE']
    loss_function = input('Input loss function (MAE | MSE | RMSE): ')
    if loss_function not in loss_list:
        print(f'{loss_function} is not supported')
        return None

    loss = 0
    sigma = 0
    for i in range(num_samples):
        target = random.uniform(0.0, 10.0)
        pred = random.uniform(0.0, 10.0)

        # loss
        if loss_function == 'MAE':
            loss = pre_mae(target, pred)
        else:  # MSE&RMSE
            loss = pre_mse(target, pred)
        sigma += loss
        print(
            f'loss name: {loss_function}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}')

    # loss final
    loss = sigma / num_samples
    # RMSE
    if loss_function == 'RMSE':
        loss = math.sqrt(loss)

    print(f'final {loss_function}: {loss}')


# RunExample
regression_loss_function()
