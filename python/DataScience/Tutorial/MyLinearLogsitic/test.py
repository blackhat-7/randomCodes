from scratch import MyLinearRegression, MyLogisticRegression, MyPreProcessor, k_fold_cross_validation, train_valid_test_split, Scoring
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import f1_score, classification_report
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


preprocessor = MyPreProcessor()


def test_linear_0():
    print('Linear Regression : Dataset 1')
    X, y = preprocessor.pre_process(0)

    k_fold_cross_validation(X, y, estimator=MyLinearRegression(loss_func="mae", learning_rate=0.5, epochs=1000), k=4)  # dataset 0 mae
    k_fold_cross_validation(X, y, estimator=MyLinearRegression(loss_func="rmse", learning_rate=0.5, epochs=1000), k=4)  # dataset 0 rmse
    k_fold_cross_validation(X, y, estimator=MyLinearRegression(loss_func="mae", learning_rate=0.5, epochs=1000, normal_loss=True), k=4)  # dataset 0 mae vs normal


def test_linear_1():
    print('Linear Regression : Dataset 2')
    X, y = preprocessor.pre_process(1)

    k_fold_cross_validation(X, y, estimator=MyLinearRegression(loss_func="mae", learning_rate=0.000005, epochs=500), k=4)  # dataset 1 mae
    k_fold_cross_validation(X, y, estimator=MyLinearRegression(loss_func="rmse", learning_rate=0.00001, epochs=500), k=4)  # dataset 1 rmse
    k_fold_cross_validation(X, y, estimator=MyLinearRegression(loss_func="mae", learning_rate=0.000005, epochs=500, normal_loss=True), k=4)  # dataset 1 mae vs normal


# 0.0001, 0.01, 10
def test_logistic():
    print('Logistic Regression')
    X, y = preprocessor.pre_process(2)
    Xtrain, ytrain, Xvalid, yvalid, Xtest, ytest = train_valid_test_split(X, y, ratio=[7, 1, 2])

    logistic1 = MyLogisticRegression(gd_func="bgd", learning_rate=10, epochs=1000)  # BGD
    logistic2 = MyLogisticRegression(gd_func="sgd", learning_rate=10, epochs=500)  # SGD
    logistic3 = SGDClassifier(loss="log", max_iter=500, alpha=0.01)
    logistic1.fit(Xtrain, ytrain, Xvalid, yvalid)
    logistic2.fit(Xtrain, ytrain, Xvalid, yvalid)
    logistic3.fit(Xtrain, ytrain)

    plt.figure(figsize=(20, 5), dpi=100)

    plt.subplot2grid((1, 2), (0, 0))
    plt.plot(range(logistic1.epochs), logistic1.loss_history[0], label="train")
    plt.plot(range(logistic1.epochs), logistic1.loss_history[1], label="test")
    plt.title(f"Train Vs Validation BGD (Loss: {logistic1.loss_func.upper()}, learning rate: {logistic1.learning_rate}, epochs: {logistic1.epochs})")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()

    plt.subplot2grid((1, 2), (0, 1))
    plt.plot(range(len(logistic2.loss_history[0])), logistic2.loss_history[0], label="Training")
    plt.plot(range(len(logistic2.loss_history[1])), logistic2.loss_history[1], label="Validation")
    plt.title(f"Train Vs Validation SGD (Loss: {logistic2.loss_func.upper()}, learning rate: {logistic2.learning_rate}, epochs: {logistic2.epochs})")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()

    plt.show()

    ypred1_train = logistic1.predict(Xtrain)
    ypred2_train = logistic2.predict(Xtrain)
    ypred3_train = logistic3.predict(Xtrain)

    ypred1_test = logistic1.predict(Xtest)
    ypred2_test = logistic2.predict(Xtest)
    ypred3_test = logistic3.predict(Xtest)

    print(f"BGD Train Accuracy : {Scoring(ytrain, ypred1_train).accuracy()}")
    print(f"BGD Test Accuracy : {Scoring(ytest, ypred1_test).accuracy()}")

    print(f"SGD Train Accuracy : {Scoring(ytrain, ypred2_train).accuracy()}")
    print(f"SGD Test Accuracy : {Scoring(ytest, ypred2_test).accuracy()}")

    print(f"SKL Train Accuracy : {Scoring(ytrain, ypred3_train).accuracy()}")
    print(f"SKL Test Accuracy : {Scoring(ytest, ypred3_test).accuracy()}")

    # print(f"BGD f1 score : {f1_score(yvalid, ypred1)}")
    # print(f"SGD f1 score : {f1_score(yvalid, ypred2)}")
    # print(f"SKL f1 score : {f1_score(yvalid, ypred3)}")

    # print(f"BGD clf report : {classification_report(yvalid, ypred1)}")
    # print(f"SGD clf report : {classification_report(yvalid, ypred2)}")
    # print(f"SKL clf report : {classification_report(yvalid, ypred3)}")


def Q4():
    clf = MyLogisticRegression(epochs=1000, learning_rate=0.1, gd_func="bgd")
    clf.fit(X, y)
    print(clf.coeffs)
    print(clf.predict(np.array([[75.0, 2.0, 1]])))
    print(np.exp(0.01595119))
    print(np.exp(-0.19731202))


def analyze_bank_dataset():
    data = pd.read_csv("./data_banknote_authentication.txt", delimiter=",", header=None)
    print(data.isnull().sum())
    print("-----------------------------------------------------------------------")
    data.info()
    print("-----------------------------------------------------------------------")
    print(data.describe())


test_logistic()
