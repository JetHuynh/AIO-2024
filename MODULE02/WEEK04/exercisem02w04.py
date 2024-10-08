# -*- coding: utf-8 -*-
"""ExerciseM02W04.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11RrDYR2gRbLpQdkP9i8r7vaKQhxci2n3

# 1. BASIC PROBABILITY

## Câu hỏi 1: Kết quả của đoạn chương trình tính mean sau đây là:
## Cho Data X = {2, 0, 2, 2, 7, 4, −2, 5, −1, −1}
## Hãy hoàn thiện function compute_mean() để tính mean μ của X đã cho.
"""

### Question 1
import numpy as np

def compute_mean(X):
  # your code here *********************
  result = np.sum(X)/len(X)
  return result
  # ************************************

X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print("Mean : ", compute_mean(X))

"""## Câu hỏi 2: Kết quả của đoạn chương trình tính median sau đây là:
## Cho Data X = {1, 5, 4, 4, 9, 13}. Hãy hoàn thiện function compute_median() để tìm median của X đã cho.
"""

### Question 2

def compute_median(X):
  size = len(X)
  X = np.sort(X)
  print(X)
  if (size % 2 == 0):
    result = (1/2*(X[int(size/2)-1] + (X[int(size/2) + 1 - 1])))
  else:
    result = X[int((size+1)/2)-1]
  return result

X = [1, 5, 4, 4, 9, 13]
print("Median: ", compute_median(X))

"""## Câu hỏi 3: Kết quả của đoạn chương trình tính variance và standard deviation sau đây là:
## Cho Data X = {171, 176, 155, 167, 169, 182}
## Hãy hoàn thiện function compute_std() để tìm standard deviation σ của X đã cho.
"""

### Question 3

def compute_std(X):
  mean = compute_mean(X)
  variance = 0
  # your code here *******************
  for x in X:
    variance = variance + (x - mean)**2
  variance = variance / len(X)
  # *********************************
  return np.sqrt(variance)

X = [ 171, 176, 155, 167, 169, 182]
print(np.round(compute_std(X),2))

"""## Câu hỏi 4: Kết quả của đoạn chương trình tính correlation coefficient sau đây là:
## Cho Data X = { −2, −5, −11, 6, 4, 15, 9} và
## Y = { 4, 25, 121, 36, 16, 225, 81}
## Hoàn thiện function compute_correlation_cofficient() để tìm correlation coefficient của X và Y đã cho?
"""

### Question 4

def compute_correlation_cofficient(X, Y):
  N = len(X)
  numerator = 0
  denominator = 0
  # your code here ****************
  numerator = N * X.dot(Y) - np.sum(X)*np.sum(Y)
  denominator = ( np.sqrt(N*np.sum(np.square(X))-np.sum(X)**2) )*( np.sqrt(N*np.sum(np.square(Y))-np.sum(Y)**2) )
  # ********************************
  return np.round(numerator / denominator,2)

X = np.asarray([-2, -5, -11, 6, 4, 15, 9])
Y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print("Correlation: ", compute_correlation_cofficient(X,Y))

"""# 2. TABULAR DATA ANALYSIS"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Colab Notebooks/data
!gdown 1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq

# Commented out IPython magic to ensure Python compatibility.
# %cd ..

"""## Câu hỏi 5: Kết quả của đoạn chương trình sau đây là:"""

import pandas as pd

data = pd.read_csv("./data/advertising.csv")

def correlation(x, y):
  # your code here ****************
  x_mean = np.mean(x)
  y_mean = np.mean(y)

  numerator = np.sum((x - x_mean) * (y - y_mean))
  denominator = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))

  if denominator == 0:
    result = 0
  else:
    result = numerator / denominator

  return result
  # ********************************

### Question 5
# Example usage :
x = data['TV']
y = data['Radio']

result = correlation(x, y)
print(f" Correlation between TV and Sales : { round ( result , 2)}")

"""## Câu hỏi 6: Kết quả của đoạn chương trình sau đây là:"""

### Question 6
features = ['TV', 'Radio', 'Newspaper']

for feature_1 in features:
  for feature_2 in features:
      correlation_value = correlation(data[feature_1], data[feature_2])
      print(f"Correlation between {feature_1} and {feature_2}:{round(correlation_value,2)}")

"""## Câu hỏi 7: Hãy cho biết đoạn code phù hợp với kết quả sau đây là:"""

### Question 7
data = pd.read_csv("./data/advertising.csv")
x = data['Radio']
y = data['Newspaper']

result = np.corrcoef(x, y)
print(result)
# Expected output : [[1.          0.35410375]
#                    [0.35410375  1.        ]]

"""## Câu hỏi 8: Hãy cho biết đoạn code phù hợp với kết quả sau đây là:"""

### Question 8
data = pd.read_csv("./data/advertising.csv")
# Your code here #
# Calculate the correlation matrix
data_corr_coef = data.corr()
data_corr_coef
#*****************

"""## Câu hỏi 9: Hãy cho biết đoạn code phù hợp với kết quả sau đây là:"""

### Question 9
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./data/advertising.csv")

plt.figure(figsize=(10,8))
# Your code here #
# Calculate the correlation matrix
data_corr_coef = data.corr()
# Plot the heatmap
sns.heatmap(data_corr_coef, annot=True, fmt=".2f", linewidth=.5)
#****************
plt.show()

"""# 3. TEXT RETRIEVAL"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Colab Notebooks/data
# Download dataset :
! gdown 1jh2p2DlaWsDo_vEWIcTrNh3mUuXd-cw6

# Commented out IPython magic to ensure Python compatibility.
# %cd ..

"""## Câu hỏi 10: Kết quả của đoạn chương trình đọc file và sử dụng TF-IDF để biểu diễn văn bản thành vector sau đây là:"""

### Question 10
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

vi_data_df = pd.read_csv("./data/vi_text_retrieval.csv")
context = vi_data_df['text']
context = [doc.lower() for doc in context]

tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)

context_embedded.toarray()[7][0]

"""## Câu hỏi 11: Kết quả của đoạn chương trình tính độ tương đồng cosine là:"""

### Question 11
def tfidf_search(question, tfidf_vectorizer, top_d=5):
  # lowercasing before encoding
  query_embedded = tfidf_vectorizer.transform([question.lower()])
  cosine_scores = cosine_similarity(context_embedded, query_embedded).reshape((-1,))
  results = []
  for idx in cosine_scores.argsort()[-top_d:][::-1]:
    doc = {'id': idx, 'cosine_score':cosine_scores[idx]  }
    results.append(doc)
  return results

question = vi_data_df.iloc[0]['question']
results = tfidf_search(question, tfidf_vectorizer, top_d=5)
results[0]['cosine_score']

"""## Câu hỏi 12: Kết quả của đoạn chương trình tính độ tương đồng correlation là:"""

### Question 12
def corr_search(question, tfidf_vectorizer, top_d=5):
  # lowercasing before encoding
  query_embedded = tfidf_vectorizer.transform([question.lower()])
  corr_scores = np.corrcoef( query_embedded.toarray()[0],   context_embedded.toarray() )
  corr_scores = corr_scores[0][1:]
  # Get top k correlation score and index its
  results = []
  for idx in corr_scores.argsort()[-top_d:][::-1]:
    doc = {'id': idx, 'corr_score':corr_scores[idx] }
    results.append(doc)
  return results

question = vi_data_df.iloc[0]['question']
results = corr_search(question, tfidf_vectorizer, top_d=5)
results[1]['corr_score']









