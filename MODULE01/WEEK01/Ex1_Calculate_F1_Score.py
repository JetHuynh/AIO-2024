"""## 1. Viết function thực hiện đánh giá classification model bằng F1-Score."""
# f1 score is the evaluation metric that is used to evaluate the performance of the machine learning model
def Calculate_F1_Score(TruePositive,FalsePositive,FalseNegative):
    #validate type parameters
    if not isinstance(TruePositive, int) or not isinstance(FalsePositive, int) or not isinstance(FalseNegative, int):
        print("Input parameters must be integer")
        return None

    #validate input parameters
    if TruePositive < 0 or FalsePositive < 0 or FalseNegative < 0:
        print("Input parameters must be greater than zero")
        return None

    #calculate F1-Score
    precision = TruePositive / (TruePositive + FalsePositive)
    recall = TruePositive / (TruePositive + FalseNegative)
    f1_score = 2 * (precision * recall) / (precision + recall)

    # Print result
    print(f'\nprecision is {precision}')
    print(f'recall is {recall}')
    print(f'f1-score is {f1_score}\n')


# Examples
Calculate_F1_Score (2, 3, 4)
Calculate_F1_Score ('a', 3, 4)
Calculate_F1_Score (2, 'a', 4)
Calculate_F1_Score (2, 3, 'a')
Calculate_F1_Score (2, 3, 0)
Calculate_F1_Score (2.1 ,3 , 0)
