"""## 1. Viết function thực hiện đánh giá classification model bằng F1-Score."""
# f1 score is the evaluation metric that is used to evaluate the performance of the machine learning model


def calculate_f1_score(truepositive, falsepositive, falsenegative):
    # validate type parameters
    if not isinstance(truepositive, int) or not isinstance(falsepositive, int) or not isinstance(falsenegative, int):
        print("Input parameters must be integer")
        return None

    # validate input parameters
    if truepositive < 0 or falsepositive < 0 or falsenegative < 0:
        print("Input parameters must be greater than zero")
        return None

    # calculate F1-Score
    precision = truepositive / (truepositive + falsepositive)
    recall = truepositive / (truepositive + falsenegative)
    f1_score = 2 * (precision * recall) / (precision + recall)

    # Print result
    print(f'\nprecision is {precision}')
    print(f'recall is {recall}')
    print(f'f1-score is {f1_score}\n')


# Examples
calculate_f1_score(2, 3, 4)
calculate_f1_score('a', 3, 4)
calculate_f1_score(2, 'a', 4)
calculate_f1_score(2, 3, 'a')
calculate_f1_score(2, 3, 0)
calculate_f1_score(2.1, 3, 0)
