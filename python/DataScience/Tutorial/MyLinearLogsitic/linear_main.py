import pandas as pd
import numpy as np
from scratch import MyLinearRegression
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR


def clean_data(data):
    data["User_Score"] = data["User_Score"].dropna().apply(lambda x: float(x) if x.isdigit() else float("NaN"))
    data["User_Score"] = data["User_Score"].fillna(data["User_Score"].dropna().mean())
    data["Critic_Score"] = data["Critic_Score"].fillna(data["Critic_Score"].dropna().mean())
    return data


data = pd.read_csv("./VideoGameDataset - Video_Games_Sales_as_at_22_Dec_2016.csv")
data = data[["Critic_Score", "User_Score", "Global_Sales"]]
# print(data.head(5))
# print(data.shape)

data = clean_data(data)

print(data.info())
print(data.head(5))

X = data[["Critic_Score", "User_Score"]]
y = data[["Global_Sales"]]
X = np.array(X)
y = np.array(y)

clf_linear = MyLinearRegression(error="mae", learning_rate=0.1)
clf_linear.fit(X, y)
print(X[0].shape)
X_test = np.array([[76, 8]])
print(clf_linear.predict(X_test))
