# -*- coding: utf-8 -*-
"""ExerciseM02W03.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YYT6Ti7mWxxPabpOg6TknyAM1nd2yHXj

# 4.1 Hoàn thiện function create_train_dataset() để tổ chức dữ liệu bảng 1 vào array 2 chiều như bên dưới
"""

#########################
# Create data
#########################
import numpy as np

def create_train_data():
  data=[['Sunny','Hot', 'High', 'Weak', 'no'],
        ['Sunny','Hot', 'High', 'Strong', 'no'],
        ['Overcast','Hot', 'High', 'Weak', 'yes'],
        ['Rain','Mild', 'High', 'Weak', 'yes'],
        ['Rain','Cool', 'Normal', 'Weak', 'yes'],
        ['Rain','Cool', 'Normal', 'Strong', 'no'],
        ['Overcast','Cool', 'Normal', 'Strong', 'yes'],
        ['Overcast','Mild', 'High', 'Weak', 'no'],
        ['Sunny','Cool', 'Normal', 'Weak', 'yes'],
        ['Rain','Mild', 'Normal', 'Weak', 'yes']
        ]
  return np.array(data)

#view data
train_data = create_train_data()
print(train_data)

"""# 4.2 Hoàn thiện function compute_prior_probability tính P("Play Tennis" = "Yes") and tính P("Play Tennis" = "No") như bên dưới:"""

# compute prior probablity
def compute_prior_probablity(train_data):
  y_unique = ['no', 'yes']
  prior_probability = np.zeros(len(y_unique))
  for i in range(len(y_unique)):
    prior_probability[i] = len(train_data[train_data[:, -1] == y_unique[i]]) / len(train_data)
  return prior_probability

# test function - Câu hỏi 14
prior_probablity = compute_prior_probablity(train_data)
print("P(“Play Tennis” = No)", prior_probablity[0])
print("P(“Play Tennis” = Yes)", prior_probablity[1])

"""# 4.3 Hoàn thiện function compute_conditional_probability để tính likelihood (The probability of "A" being True. Given "B" True, P(A|B)) như bên dưới:"""

# compute conditional probability
def compute_conditional_probability(train_data):
  y_unique = ['no', 'yes']
  conditional_probability = []
  list_x_name = []
  for i in range(0, len(train_data[0]) - 1):
    x_unique = np.unique(train_data[:, i])
    list_x_name.append(x_unique)
    print(x_unique)

    x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))
    for j in range(len(y_unique)):
      for k in range(len(x_unique)):
        x_conditional_probability[j, k] = len(train_data[(train_data[:, i] == x_unique[k]) & (train_data[:, -1] == y_unique[j])])/len(train_data[train_data[:, -1] == y_unique[j]])
    conditional_probability.append(x_conditional_probability)
  return conditional_probability, list_x_name

# test function - Câu hỏi 15
train_data = create_train_data()
_, list_x_name  = compute_conditional_probability(train_data)
print("x1 = ",list_x_name[0])
print("x2 = ",list_x_name[1])
print("x3 = ",list_x_name[2])
print("x4 = ",list_x_name[3])

"""# 4.4 Hoàn thiện function get_index_from_value để tính trả về index tương ứng với feature name:"""

#This function is used to return the index of the feature name
def get_index_from_value(feature_name, list_features):
  return np.where(list_features == feature_name)[0][0]

#test function - Câu hỏi 16
train_data = create_train_data()
_, list_x_name  = compute_conditional_probability(train_data)
outlook = list_x_name[0]
i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)

print(i1, i2, i3)

# test function - Câu hỏi 17
train_data = create_train_data()
conditional_probability, list_x_name  = compute_conditional_probability(train_data)
# Compute P("Outlook"="Sunny"|Play Tennis"="Yes")
x1=get_index_from_value("Sunny",list_x_name[0])
print("P('Outlook'='Sunny'|Play Tennis'='Yes') = ", np.round(conditional_probability[0][1, x1],2))

# test function - Câu hỏi 18
train_data = create_train_data()
conditional_probability, list_x_name  = compute_conditional_probability(train_data)
# Compute P("Outlook"="Sunny"|Play Tennis"="No")
x1=get_index_from_value("Sunny",list_x_name[0])
print("P('Outlook'='Sunny'|Play Tennis'='No') = ", np.round(conditional_probability[0][0, x1],2))

"""# 4.5 Hoàn thiện function train_naive_bayes như bên dưới:"""

###########################
# Train Naive Bayes Model
###########################
def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name  = compute_conditional_probability(train_data)

    return prior_probability,conditional_probability, list_x_name

# test function
data = create_train_data()
prior_probability,conditional_probability, list_x_name = train_naive_bayes(data)

"""# 4.6 Hoàn thiện function prediction_play_tennis để hỗ trợ AD có nên đi chơi tennis vào ngày D11 không"""

####################
# Prediction
####################
def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):

    x1=get_index_from_value(X[0],list_x_name[0])
    x2=get_index_from_value(X[1],list_x_name[1])
    x3=get_index_from_value(X[2],list_x_name[2])
    x4=get_index_from_value(X[3],list_x_name[3])

    p0 = prior_probability[0] \
    * conditional_probability[0][0, x1] \
    * conditional_probability[1][0, x2] \
    * conditional_probability[2][0, x3] \
    * conditional_probability[3][0, x4]

    p1 = prior_probability[1] \
    * conditional_probability[0][1, x1] \
    * conditional_probability[1][1, x2] \
    * conditional_probability[2][1, x3] \
    * conditional_probability[3][1, x4]

    if p0 > p1:
        y_predict = 0
    else:
        y_predict = 1

    return y_predict

#test function - Câu hỏi 19
X = ['Sunny','Cool', 'High', 'Strong']
data = create_train_data()
prior_probability,conditional_probability, list_x_name = train_naive_bayes(data)
pred =  prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability)

if(pred):
  print("Ad should go!")
else:
  print("Ad should not go!")

"""# IRIS CLASSIFIER IMPLEMENTATION"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Colab Notebooks/data

!gdown '1z7hStO6RCOlVmo-YE0O1hwQ2swItvCPa'

# create train data iris
def create_train_data_iris():
  data = np.loadtxt("./data/iris.data.txt", delimiter=",", dtype=str)
  return data

# Commented out IPython magic to ensure Python compatibility.
# %cd ..

#view data
train_data_iris = create_train_data_iris()
print(train_data_iris)

#compute prior probablity iris
def compute_prior_probablity_iris(train_data):
  y_unique = np.unique(train_data[:, -1])
  prior_probability = np.zeros(len(y_unique))
  for i in range(len(y_unique)):
    prior_probability[i] = len(train_data[train_data[:, -1] == y_unique[i]]) / len(train_data)
  return prior_probability

# compute conditional probability iris
import numpy as np

def compute_conditional_probability_iris(train_data):
  y_unique = np.unique(train_data[:, -1])
  conditional_probability = []
  list_x_name = []
  for i in range(0, len(train_data[0]) - 1):
    x_conditional_probability_iris = np.zeros((len(y_unique),2))
    for j in range(0,len(y_unique)):
      mean = np.mean(train_data[train_data[:, -1] == y_unique[j], i].astype(float))
      std = np.std(train_data[train_data[:, -1] == y_unique[j], i].astype(float))
      x_conditional_probability_iris[j, 0] = mean
      x_conditional_probability_iris[j, 1] = std
    conditional_probability.append(x_conditional_probability_iris)
  return conditional_probability

import math
#Define the Gaussian function
def gauss(x, mean, sigma):
  result = (1/(math.sqrt(2*math.pi)*sigma))\
  *(math.exp(-((x-mean)**2)/(2*sigma**2)))
  return result

#train gaussian naive bayes
def train_gaussian_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity_iris(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability = compute_conditional_probability_iris(train_data)
    return prior_probability,conditional_probability

# prediction iris
def prediction_iris(X,  prior_probability, conditional_probability):
    p0=prior_probability[0] \
    *gauss(X[0], conditional_probability[0][0][0],conditional_probability[0][0][1])  \
    *gauss(X[1], conditional_probability[1][0][0],conditional_probability[1][0][1])  \
    *gauss(X[2], conditional_probability[2][0][0],conditional_probability[2][0][1])  \
    *gauss(X[3], conditional_probability[3][0][0],conditional_probability[3][0][1])

    p1=prior_probability[1] \
    *gauss(X[0], conditional_probability[0][1][0],conditional_probability[0][1][1])  \
    *gauss(X[1], conditional_probability[1][1][0],conditional_probability[1][1][1])  \
    *gauss(X[2], conditional_probability[2][1][0],conditional_probability[2][1][1])  \
    *gauss(X[3], conditional_probability[3][1][0],conditional_probability[3][1][1])

    p2=prior_probability[2] \
    *gauss(X[0], conditional_probability[0][2][0],conditional_probability[0][2][1])  \
    *gauss(X[1], conditional_probability[1][2][0],conditional_probability[1][2][1])  \
    *gauss(X[2], conditional_probability[2][2][0],conditional_probability[2][2][1])  \
    *gauss(X[3], conditional_probability[3][2][0],conditional_probability[3][2][1])

    list_p = [p0,p1,p2]
    y_predict = np.argmax(list_p)
    return y_predict

#Example 1 #########################
X = [6.3 , 3.3, 6.0,  2.5]
train_data = create_train_data_iris()
y_unique = np.unique(train_data[:,4])
prior_probability, conditional_probability = train_gaussian_naive_bayes(train_data)
pred = y_unique[prediction_iris(X, prior_probability, conditional_probability)]
print(pred)
assert pred == "Iris-virginica"

#Example 2 #########################
X = [5.0,2.0,3.5,1.0]
train_data = create_train_data_iris()
y_unique = np.unique(train_data[:,4])
prior_probability, conditional_probability = train_gaussian_naive_bayes(train_data)
pred = y_unique[prediction_iris(X, prior_probability, conditional_probability)]
print(pred)
assert pred == "Iris-versicolor"

#Example 3 #########################
# X =[sepal length, sepal width, petal length, petal width]
X = [4.9,3.1,1.5,0.1]
train_data = create_train_data_iris()
y_unique = np.unique(train_data[:,4])
prior_probability, conditional_probability = train_gaussian_naive_bayes(train_data)
pred = y_unique[prediction_iris(X, prior_probability, conditional_probability)]
print(pred)
assert pred == "Iris-setosa"



