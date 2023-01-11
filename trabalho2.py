import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import  GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier

fileName = "train.csv"
class modelo:
    @classmethod
    def predict(cls, xTeste):
       fileContent = pd.read_csv(fileName)
       X = fileContent.drop('Failure',axis='columns')
       y = fileContent['Failure']
       clf = KNeighborsClassifier(n_neighbors=3)
       clf.fit(X,y)
       return clf.predict(xTeste)

class modelo2:
    @classmethod
    def predict(cls, xTeste):
        fileContent = pd.read_csv(fileName)
        X = fileContent.drop('Failure', axis='columns')
        y = fileContent['Failure']
        clf = GaussianNB()
        clf.fit(X,y)
        return clf.predict(xTeste)


# Metodo Linear não esta a funcionar
class modelo3:
    @classmethod
    def predict(cls,xTeste):
        fileContent = pd.read_csv(fileName)
        X = fileContent.drop('Failure', axis='columns')
        y = fileContent['Failure']
        clf = DecisionTreeClassifier()
        clf.fit(X,y)
        return clf.predict(xTeste)

class modelo4:
    @classmethod
    def predict(cls, xTeste):
        fileContent = pd.read_csv(fileName)
        X = fileContent.drop('Failure', axis='columns')
        y = fileContent['Failure']
        clf = BaggingClassifier()
        clf.fit(X,y)
        return clf.predict(xTeste)

class modelo5:
    @classmethod
    def predict(cls, xTeste):
        fileContent = pd.read_csv(fileName)
        X = fileContent.drop('Failure', axis='columns')
        y = fileContent['Failure']
        clf = RandomForestClassifier(n_estimators=500)
        clf.fit(X,y)
        return clf.predict(xTeste)

class modelo6:
    @classmethod
    def predict(cls, xTeste):
        fileContent = pd.read_csv(fileName)
        X = fileContent.drop('Failure', axis='columns')
        y = fileContent['Failure']
        clf = ExtraTreeClassifier()
        clf.fit(X,y)
        return clf.predict(xTeste)

class modelo7:
    @classmethod
    def predict(cls, xTeste):
        fileContent = pd.read_csv(fileName)
        X = fileContent.drop('Failure', axis='columns')
        y = fileContent['Failure']
        clf = GradientBoostingClassifier()
        clf.fit(X,y)
        return clf.predict(xTeste)


