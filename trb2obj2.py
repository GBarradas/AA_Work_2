import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import ExtraTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier

# Calcular a media e criar o novo conjunto de dados
def tratamentoDados(X):
    y ={}
    y['Id'] = X['Id']
    y['Program'] = X['Program']
    y['media'] = (X['Y1s1_grade']+X['Y1s2_grade']+ \
                  X['Y2s1_grade']+X['Y2s2_grade']+ \
                  X['Y3s1_grade']+X['Y3s2_grade']+ \
                  X['Y4s1_grade']+X['Y4s2_grade'])/8
    return pd.DataFrame.from_dict(y,orient='columns')
fileName = "train.csv"

# K-Neighbors
class modelo:
    @classmethod
    def predict(cls, xTeste):
       fileContent = pd.read_csv(fileName)

       X = tratamentoDados(fileContent)
       y = fileContent['Failure']
       clf = KNeighborsClassifier(n_neighbors=3)
       clf.fit(X,y)
       return clf.predict(xTeste)

# Naive Bayes
class modelo2:
    @classmethod
    def predict(cls, xTeste):
        fileContent = pd.read_csv(fileName)
        X = tratamentoDados(fileContent)
        y = fileContent['Failure']
        print(X)
        clf = GaussianNB()
        clf.fit(X,y)
        return clf.predict(xTeste)


# Decision Tree Classifier
class modelo3:
    @classmethod
    def predict(cls,xTeste):
        fileContent = pd.read_csv(fileName)
        X = tratamentoDados(fileContent)
        y = fileContent['Failure']
        clf = DecisionTreeClassifier()
        clf.fit(X,y)
        return clf.predict(xTeste)

# Bagging Classifier
class modelo4:
    @classmethod
    def predict(cls, xTeste):
        fileContent = pd.read_csv(fileName)
        X = tratamentoDados(fileContent)
        y = fileContent['Failure']
        clf = BaggingClassifier()
        clf.fit(X,y)
        return clf.predict(xTeste)

# Random Forest Classifier
class modelo5:
    @classmethod
    def predict(cls, xTeste):
        fileContent = pd.read_csv(fileName)
        X = tratamentoDados(fileContent)
        y = fileContent['Failure']
        clf = RandomForestClassifier(n_estimators=500)
        clf.fit(X,y)
        return clf.predict(xTeste)

# Extra Tree Classifier
class modelo6:
    @classmethod
    def predict(cls, xTeste):
        fileContent = pd.read_csv(fileName)
        X = tratamentoDados(fileContent)
        y = fileContent['Failure']
        clf = ExtraTreeClassifier()
        clf.fit(X,y)
        return clf.predict(xTeste)

#Gradient Boosting Classifier
class modelo7:
    @classmethod
    def predict(cls, xTeste):
        fileContent = pd.read_csv(fileName)
        X = tratamentoDados(fileContent)
        y = fileContent['Failure']
        clf = GradientBoostingClassifier()
        clf.fit(X,y)
        return clf.predict(xTeste)


