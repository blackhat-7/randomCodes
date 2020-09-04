import pandas as pd


def clean(train):
    train["Fare"] = train["Fare"].fillna(train["Fare"].dropna().median())
    train["Age"] = train["Age"].fillna(train["Age"].dropna().median())

    train.loc[train['Sex']=='male', "Sex"] = 0
    train.loc[train['Sex']=='female', "Sex"] = 1

    train["Embarked"] = train["Embarked"].fillna(train["Embarked"].dropna().mode()[0])
    train.loc[train["Embarked"] == "S", "Embarked"] = 0
    train.loc[train["Embarked"] == "C", "Embarked"] = 1
    train.loc[train["Embarked"] == "Q", "Embarked"] = 2




