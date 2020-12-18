import numpy as np
import pandas as pd
from random import sample
import matplotlib.pyplot as plt
import math


class MyPreProcessor():
    """
    My steps for pre-processing for the three datasets.
    """

    def __init__(self, ):
        pass

    def pre_process(self, dataset):
        """
        Reading the file and preprocessing the input and output.
        Note that you will encode any string value and/or remove empty entries in this function only.
        Further any pre processing steps have to be performed in this function too.

        Parameters
        ----------

        dataset : integer with acceptable values 0, 1, or 2
        0 -> Abalone Dataset
        1 -> VideoGame Dataset
        2 -> BankNote Authentication Dataset

        Returns
        -------
        X : 2-dimensional numpy array of shape (n_samples, n_features)
        y : 1-dimensional numpy array of shape (n_samples,)
        """

        # np.empty creates an empty array only. You have to replace this with your code.
        X = np.empty((0, 0))
        y = np.empty((0))

        if dataset == 0:
            data = pd.read_csv("abalone/Dataset.data", delimiter=" ", header=None)
            data[0] = data[0].apply(lambda x: 0 if x == 'M' else 1 if x == 'F' else 2)
            data = data.sample(frac=1, random_state=42).reset_index(drop=True)
            X = np.array(data[list(range(8))])
            y = np.array(data[8])

        elif dataset == 1:
            # Implement for the video game dataset
            data = pd.read_csv("./VideoGameDataset - Video_Games_Sales_as_at_22_Dec_2016.csv")
            data = data[["Critic_Score", "User_Score", "Global_Sales"]]
            data = data.sample(frac=1, random_state=42).reset_index(drop=True)
            data.replace(to_replace='tbd', value=np.NaN, inplace=True)
            data.dropna(subset=["Critic_Score", "User_Score"], inplace=True)
            X = np.array(data[["Critic_Score", "User_Score"]], dtype=float)
            y = np.array(data[["Global_Sales"]])

        elif dataset == 2:
            # Implement for the banknote authentication dataset
            data = pd.read_csv("./data_banknote_authentication.txt", delimiter=",", header=None)
            data = data.sample(frac=1, random_state=42).reset_index(drop=True)
            X = np.array(data[list(range(4))])
            y = np.array(data[4])

        return X, y


class MyLinearRegression():
    """
    My implementation of Linear Regression.

    Parameters
    ----------
    learning_rate: default=0.01, Rate at which the model learns.

    epochs: default=100, number of iterations to train the model.

    loss_func: {'mae','rmse'}, default='mae', Loss function used to calculate loss.

    normal_form: {True, False}, default=False, Whether to use normal form to calculate the coefficients.

    Returns
    -------
    an instance of MyLinearRegression
    """

    def __init__(self, learning_rate=0.01, epochs=100, loss_func="mae"):
        self.X = None
        self.y = None
        self.coeff = None
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.loss_func = loss_func
        self.loss_history = [[], []]
        self.normal_coeff = None

    def fit(self, X, y, Xtest=None, ytest=None, normal_loss=False):
        """
        Fitting (training) the linear model.

        Parameters
        ----------
        X : 2-dimensional numpy arsray of shape (n_samples, n_features) which acts as training data.

        y : 1-dimensional numpy array of shape (n_samples,) which acts as training labels.

        Xtest: default=None, 2-dimentional numpy array which acts as the test data.

        ytest: default=None, 1-dimentional numpy array which acts as the test labels.

        Returns
        -------
        self : an instance of self
        """
        ones = np.ones((X.shape[0], 1))
        X = np.hstack((ones, X))
        y = y.reshape(-1, 1)
        n_samples, n_features = X.shape

        if Xtest is not None:
            ones = np.ones((Xtest.shape[0], 1))
            Xtest = np.hstack((ones, Xtest))
            ytest = ytest.reshape(-1, 1)

        if (n_samples != y.shape[0]):
            print("Inconsistent samples in X and y")
            return None

        self.X = X
        self.y = y
        self.initialize_parameters(n_features)
        self.loss_history = [[], []]

        # For calulating optimal parameters
        if normal_loss:
            self.normal_coeff = np.dot(np.dot(np.linalg.inv(np.dot(self.X.T, self.X)), self.X.T), self.y)
            training_loss, validation_loss = self.cost_function(n_samples, n_features, Xtest=Xtest, ytest=ytest)
            print(f"Optimal parameters: {str(self.normal_coeff)}")

        print(f"{self.loss_func} loss")
        for epoch in range(self.epochs):
            # Gradient Descent
            self.update_coeffs(n_samples, n_features)

            # Calculate Cost
            training_loss, validation_loss = self.cost_function(n_samples, n_features, Xtest=Xtest, ytest=ytest, normal_loss=normal_loss)
            self.loss_history[0].append(training_loss)
            self.loss_history[1].append(validation_loss)

            # Progress
            # print("epoch: %d      coeff: %s      cost: %.4f" % (epoch, str(self.coeff.reshape(1, -1)[0]), training_loss))

        return self

    def predict(self, X):
        """
        Predicting values using the trained linear model.

        Parameters
        ----------
        X : 2-dimensional numpy array of shape (n_samples, n_features) which acts as testing data.

        Returns
        -------
        y : 1-dimensional numpy array of shape (n_samples,) which contains the predicted values.
        """
        ones = np.ones((X.shape[0], 1))
        X = np.hstack((ones, X))

        # return the numpy array y which contains the predicted values
        return np.dot(X, self.coeff).reshape(-1,)

    def initialize_parameters(self, n_features):
        """
        Initialize coefficients.

        Parameters
        ----------
        n_features: number of features in the training set

        Returns
        -------
        None
        """
        self.coeff = np.zeros((n_features, 1))

    def update_coeffs(self, n_samples, n_features):
        """
        Updates the coefficients

        Parameters
        ----------
        n_samples: number of samples in training set

        n_features: number of features in training set

        Returns
        -------
        None
        """
        d_coeff = np.zeros((n_features, 1))
        # Gradient descent using rmse
        if self.loss_func == "rmse":
            d_coeff = (1/n_samples) * np.sum((self.X*(np.dot(self.X, self.coeff) - self.y)) / np.sqrt(np.sum((np.dot(self.X, self.coeff) - self.y)**2) / n_samples), axis=0)

        # Gradient descent using mae
        elif self.loss_func == "mae":
            loss = np.dot(self.X, self.coeff) - self.y
            loss[loss >= 0] = 1
            loss[loss < 0] = -1
            d_coeff = np.sum(self.X * loss, axis=0) / n_samples

        d_coeff = d_coeff.reshape(-1, 1)
        self.coeff -= d_coeff * self.learning_rate

    def cost_function(self, n_samples, n_features, Xtest=None, ytest=None, normal_loss=False):
        """
        Computes the cost of Training data to Training labels and Test data to Test labels if provided.

        Parameters
        ----------
        n_samples: number of samples in training set

        n_features: number of features in training set

        Xtest: default=None, 2-dimentional numpy array which acts as the test data

        ytest: default=None, 1-dimentional numpy array which acts as the test labels

        Returns
        -------
        training_loss (cost of training), validation_loss (cost of test data if provided else none)
        """
        validation_loss = None

        # Compute loss with respect to optimal parameters
        if normal_loss:
            normal_pred = np.dot(self.X, self.normal_coeff)
            training_loss = np.sum(np.abs(np.dot(self.X, self.coeff) - normal_pred), axis=0) / n_samples
            if Xtest is not None:
                normal_pred = np.dot(Xtest, self.normal_coeff)
                validation_loss = np.sum(np.abs(np.dot(Xtest, self.coeff) - normal_pred), axis=0) / Xtest.shape[0]

        # Compute RMSE
        elif self.loss_func == "rmse":
            training_loss = np.sqrt(np.sum((np.dot(self.X, self.coeff) - self.y)**2, axis=0) / n_samples)
            if Xtest is not None:
                validation_loss = np.sqrt(np.sum((np.dot(Xtest, self.coeff) - ytest)**2, axis=0) / Xtest.shape[0])

        # Compute MAE
        elif self.loss_func == "mae":
            training_loss = np.sum(np.abs(np.dot(self.X, self.coeff) - self.y), axis=0) / n_samples
            if Xtest is not None:
                validation_loss = np.sum(np.abs(np.dot(Xtest, self.coeff) - ytest), axis=0) / Xtest.shape[0]

        return training_loss, validation_loss


class MyLogisticRegression():
    """
    My implementation of Logistic Regression.

    Parameters
    ----------
    learning_rate: default=10, Rate at which the model learns

    epochs: default=100, number of iterations to train the model

    loss_func: {'logloss'}, default='logloss', Loss function used to calculate loss

    gd_func: {'sgd', 'bgd'}, default='sgd', Function used to perform gradient descent

    Returns
    -------
    an instance of MyLogisticRegression
    """

    def __init__(self, learning_rate=10, epochs=100, loss_func="logloss", gd_func="sgd"):
        self.X = None
        self.y = None
        self.coeff = None
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.loss_func = loss_func
        self.loss_history = [[], []]
        self.classes = 1
        self.gd_func = gd_func

    def fit(self, X, y, Xtest=None, ytest=None):
        """
        Fitting (training) the logistic model.

        Parameters
        ----------
        X : 2-dimensional numpy array of shape (n_samples, n_features) which acts as training data.

        y : 1-dimensional numpy array of shape (n_samples,) which acts as training labels.

        Xtest: default=None, 2-dimentional numpy array which acts as the test data

        ytest: default=None, 1-dimentional numpy array which acts as the test labels

        Returns
        -------
        self : an instance of self
        """
        ones = np.ones((X.shape[0], 1))
        X = np.hstack((ones, X))
        y = y.reshape(-1, 1)
        n_samples, n_features = X.shape

        if Xtest is not None:
            ones = np.ones((Xtest.shape[0], 1))
            Xtest = np.hstack((ones, Xtest))
            ytest = ytest.reshape(-1, 1)

        if (n_samples != y.shape[0]):
            print("Inconsistent samples in X and y")
            return None

        self.classes = np.unique(y).shape[0]
        self.X = X
        self.y = y
        self.initialize_parameters(n_features)
        self.loss_history = [[], []]

        # Batch Gradient descent
        if self.gd_func == "bgd":
            self.batch_gradient_descent(n_samples, n_features, Xtest, ytest)

        # Stochastic Gradient descent
        elif self.gd_func == "sgd":
            self.stochastic_gradient_descent(n_samples, n_features, Xtest, ytest)

        return self

    def predict(self, X):
        """
        Predicting values using the trained logistic model.

        Parameters
        ----------
        X : 2-dimensional numpy array of shape (n_samples, n_features) which acts as testing data.

        Returns
        -------
        y : 1-dimensional numpy array of shape (n_samples,) which contains the predicted values.
        """
        ones = np.ones((X.shape[0], 1))
        X = np.hstack((ones, X))
        y_prob = 1 / (1 + np.exp(-np.dot(X, self.coeff)))
        # return the numpy array y which contains the predicted values
        return self.classify(y_prob).reshape(-1, )

    def batch_gradient_descent(self, n_samples, n_features, Xtest=None, ytest=None):
        """
        Batch gradient descent, applying gradient descent on every sample simultaneously

        Parameters
        ----------
        n_samples: number of samples in training set

        n_features: number of features in training set

        Xtest: default=None, 2-dimentional numpy array which acts as the test data

        ytest: default=None, 1-dimentional numpy array which acts as the test labels

        Returns
        -------
        None
        """
        for epoch in range(self.epochs):
            # Gradient Descent
            self.update_coeffs(self.X, self.y, n_samples, n_features)

            # Calculate Cost
            training_loss, validation_loss = self.cost_function(n_samples, n_features, Xtest=Xtest, ytest=ytest)
            self.loss_history[0].append(training_loss)
            self.loss_history[1].append(validation_loss)

            # Progress
            # print("epoch: %d      coeff: %s      cost: %.4f" % (epoch, str(self.coeff.reshape(1, -1)[0]), training_loss))

    def stochastic_gradient_descent(self, n_samples, n_features, Xtest=None, ytest=None):
        """
        Stochastic gradient descent, applying gradient descent on one sample at a time

        Parameters
        ----------
        n_samples: number of samples in training set

        n_features: number of features in training set

        Xtest: default=None, 2-dimentional numpy array which acts as the test data

        ytest: default=None, 1-dimentional numpy array which acts as the test labels

        Returns
        -------
        None
        """
        y_X = np.hstack((self.y, self.X))
        for epoch in range(self.epochs):
            np.random.shuffle(y_X)
            for row in y_X:
                y, X = np.hsplit(row, [1])
                y = y.reshape(1, 1)
                X = X.reshape(1, n_features)
                # Gradient Descent
                self.update_coeffs(X, y, n_samples, n_features)

            # Calculate Cost
            training_loss, validation_loss = self.cost_function(n_samples, n_features, Xtest=Xtest, ytest=ytest)
            self.loss_history[0].append(training_loss)
            self.loss_history[1].append(validation_loss)

            # Progress
            # print("epoch: %d      coeff: %s      cost: %.4f" % (epoch, str(self.coeff.reshape(1, -1)[0]), training_loss))

    def update_coeffs(self, X, y, n_samples, n_features):
        """
        Updates the coefficients

        Parameters
        ----------
        X : 2-dimensional numpy array of shape (n_samples, n_features) which acts as training data.

        y : 1-dimensional numpy array of shape (n_samples, 1) which acts as training labels.

        n_samples: number of samples in training set

        n_features: number of features in training set

        Returns
        -------
        None
        """
        hypo_x = 1 / (1 + np.exp(-np.dot(X, self.coeff)))
        d_coeff = np.sum(np.dot(X.T, (hypo_x - y)), axis=1).reshape(-1, 1)
        self.coeff -= (d_coeff / len(X)) * self.learning_rate

    def initialize_parameters(self, n_features):
        """
        Initialize coefficients

        Parameters
        ----------
        n_features: number of features in the training set

        Returns
        -------
        None
        """
        self.coeff = np.zeros((n_features, 1))

    def cost_function(self, n_samples, n_features, Xtest=None, ytest=None):
        """
        Computes the cost of Training data to Training labels and Test data to Test labels if provided

        Parameters
        ----------
        n_samples: number of samples in training set

        n_features: number of features in training set

        Xtest: default=None, 2-dimentional numpy array which acts as the test data

        ytest: default=None, 1-dimentional numpy array which acts as the test labels

        Returns
        -------
        training_loss (cost of training) and validation_loss (cost of test data if provided else none)
        """
        epsilon = 10**-9
        hypo_x = 1 / (1 + np.exp(-np.dot(self.X, self.coeff)))
        training_loss = -(1 / n_samples) * np.sum(np.dot(self.y.T, np.log(hypo_x + epsilon)) + np.dot((1 - self.y).T, np.log(1 - hypo_x + epsilon)))

        validation_loss = None
        if Xtest is not None:
            hypo_x_test = 1 / (1 + np.exp(-np.dot(Xtest, self.coeff)))
            validation_loss = -(1 / len(Xtest)) * np.sum(np.dot(ytest.T, np.log(hypo_x_test + epsilon)) + np.dot((1 - ytest).T, np.log(1 - hypo_x_test + epsilon)))

        return training_loss, validation_loss

    def classify(self, probab):
        """
        Binary Classification based on given probability

        Parameters
        ----------
        probab: A probability number in the range [0,1]

        Returns
        -------
        Binary class based on probability
        """
        probab[probab < 0.5] = 0
        probab[probab >= 0.5] = 1
        return probab


def k_fold_cross_validation(X, y, estimator=MyLinearRegression(), k=4):
    """
    Divides the train data and label into k segments and using each segment as test and rest of them as training data fits the given estimator, prints the minimum train and test cost in each fold and plots the mean train vs validation cost per iteration.

    Parameters
    ----------
    X: 2-dimentional numpy array which acts as the train data

    y: 1-dimentional numpy array which acts as the train labels

    estimator: The model used to fit data, default: MyLinearRegression()

    k: number of folds, default: 5

    Returns
    -------
    The estimator that was provided, after performing the k fold cross validation
    """
    y = y.reshape(-1, 1)
    y_X = np.hstack((y, X))
    np.random.shuffle(y_X)
    y, X = np.hsplit(y_X, [1])
    n = len(X)
    test_size = n//k
    loss_histories = [[], [], [[], []]]

    # Compute costs of each fold
    for fold in range(k):
        test_rows = list(range(fold*test_size, fold*test_size+test_size))
        Xtest = np.array([X[i] for i in test_rows])
        ytest = np.array([y[i] for i in test_rows])
        Xtrain = np.delete(X, test_rows, axis=0)
        ytrain = np.delete(y, test_rows, axis=0)
        estimator.fit(Xtrain, ytrain, Xtest=Xtest, ytest=ytest)
        loss_histories[0].append(estimator.loss_history[0])
        loss_histories[1].append(estimator.loss_history[1])
        estimator.fit(Xtrain, ytrain, Xtest=Xtest, ytest=ytest, normal_loss=True)
        loss_histories[2][0].append(estimator.loss_history[0])
        loss_histories[2][1].append(estimator.loss_history[1])

    # Plot per Fold
    plt.figure(figsize=(30, 20), dpi=80)
    row = math.ceil(k**0.5)
    col = math.ceil(k**0.5)
    m, n = 0, 0
    for i in range(k):
        plt.subplot2grid((row, col), (m, n))
        n += 1
        if n == col:
            n = 0
            m += 1
        plt.plot(range(estimator.epochs), loss_histories[0][i], label="Training")
        plt.plot(range(estimator.epochs), loss_histories[1][i], label="Validation")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.legend()
        plt.title(f"Train Vs Validation Loss {i+1} (Loss: {estimator.loss_func.upper()}, learning rate: {estimator.learning_rate}, epochs: {estimator.epochs})")
    plt.show()

    # Output min cost of every fold
    for i in range(k):
        print(f"Fold number {i+1}")
        print(f"Min train cost achieved : {min(loss_histories[0][i])}")
        print(f"Min test cost achieved : {min(loss_histories[1][i])}")
        print(f"Train loss vs optimal parameters: {min(loss_histories[2][0][i])}", )
        print(f"Test loss vs optimal parameters: {min(loss_histories[2][1][i])}\n")

    # Mean cost from all the folds
    train_loss_mean = np.mean(loss_histories[0], axis=0)
    test_loss_mean = np.mean(loss_histories[1], axis=0)
    plt.figure(figsize=(8, 5), dpi=150)
    plt.plot(range(estimator.epochs), train_loss_mean, label="Training")
    plt.plot(range(estimator.epochs), test_loss_mean, label="Validation")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title(f"Train Vs Validation {k} Fold (Loss: {estimator.loss_func.upper()}, learning rate: {estimator.learning_rate}, epochs: {estimator.epochs})")
    plt.legend()
    plt.show()

    return estimator


def train_valid_test_split(X, y, ratio=[7, 1, 2]):
    """
    Splits the given train data and train labels into training, validation and test sets according to the given ratio.

    Parameters
    ----------
    X: 2-dimentional numpy array which acts as the train data

    y: 1-dimentional numpy array which acts as the train labels

    ratio: default=[7, 1, 2], 1-dimentional array of size 3, each number denoting the ratio in which to split the given data and labels

    Returns
    -------
    Xtrain, ytrain, Xvalid, yvalid, Xtest, ytest (All the X's and y's of train, validation and test sets)
    """
    temp_X = X[:]
    temp_y = y[:]
    total = sum(ratio)
    # Test split
    test_rows = sample(range(0, len(X)), int(len(X) * ratio[2]/total))
    Xtest = np.array([temp_X[i] for i in test_rows])
    ytest = np.array([temp_y[i] for i in test_rows])
    temp_X = np.delete(temp_X, test_rows, axis=0)
    temp_y = np.delete(temp_y, test_rows, axis=0)

    # Validation split
    valid_rows = sample(range(0, len(temp_X)), int(len(X) * ratio[1]/total))
    Xvalid = np.array([temp_X[i] for i in valid_rows])
    yvalid = np.array([temp_y[i] for i in valid_rows])

    # Rest of the rows are Training
    Xtrain = np.delete(temp_X, valid_rows, axis=0)
    ytrain = np.delete(temp_y, valid_rows, axis=0)

    return Xtrain, ytrain, Xvalid, yvalid, Xtest, ytest


class Scoring:
    """
    My class with various scoring methods for ML models
    """

    def __init__(self, ytest, ypred):
        self.ytest = ytest
        self.ypred = ypred
        self.TP, self.TN, self.FP, self.FN = 0, 0, 0, 0
        self.fill()

    def fill(self):
        for ytest, ypred in zip(self.ytest, self.ypred):
            if ytest == ypred:
                if ytest == 1:
                    self.TP += 1
                else:
                    self.TN += 1
            else:
                if ytest == 1:
                    self.FN += 1
                else:
                    self.FP += 1

    def accuracy(self):
        """
        Accuracy = (TP+TN)/(TP+TN+FP+FN)
        """
        return (self.TP+self.TN)/(self.TP+self.TN+self.FP+self.FN)

    def precision(self):
        """
        Precision = TP/(TP+FP)
        """
        return self.TP/(self.TP + self.FP)

    def sensitivity(self):
        """
        Sensitivity(recall) = TP/(TP+FN)
        """
        return self.TP/(self.TP+self.FN)

    def specificity(self):
        """
        Specificity = TN/(TN+FP)
        """
        return self.TN/(self.TN+self.FP)
