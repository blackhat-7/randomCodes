import pandas as pd
import cleaner
from sklearn import linear_model, tree, model_selection

train = pd.read_csv("train.csv")
cleaner.clean(train)

print(train.head())

target = train["Survived"].values
feature_names = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
features = train[feature_names].values

decision_tree = tree.DecisionTreeClassifier(
    random_state=1,
    max_depth=7,
    min_samples_split=2
)
decision_tree_ = decision_tree.fit(features, target)

print(decision_tree_.score(features, target))

val_scores = model_selection.cross_val_score(decision_tree_, features, target, scoring="accuracy", cv=50)
print(val_scores)
print(val_scores.mean())


parameters = {'criterion': ('gini', 'entropy'), 'max_depth': (2,4,8,16,32,64), 'min_samples_split': (2,4,8,16,32,64), 'min_samples_leaf':(2,4,8,16,32,64)}

decision_tree2 = model_selection.GridSearchCV(tree.DecisionTreeClassifier(), parameters, cv=50)
decision_tree_2 = decision_tree2.fit(features, target)

print(decision_tree_2.score(features, target))

val_scores = model_selection.cross_val_score(decision_tree_2, features, target, scoring="accuracy", cv=50)
print(val_scores)
print(val_scores.mean())
