import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from trb2obj2 import modelo7 as modelo

trainFile="dropout-trabalho2.csv"
def tratamentoDados(X):
    y ={}
    y['Id'] = X['Id']
    y['Program'] = X['Program']
    y['media'] = (X['Y1s1_grade']+X['Y1s2_grade']+ \
                  X['Y2s1_grade']+X['Y2s2_grade']+ \
                  X['Y3s1_grade']+X['Y3s2_grade']+ \
                  X['Y4s1_grade']+X['Y4s2_grade'])/8
    return pd.DataFrame.from_dict(y,orient='columns')


testFile = "dropout-test.csv"
test = pd.read_csv(testFile)
X_test =  tratamentoDados(test)
y_test =  test['Failure']
y_pred_test = modelo.predict(X_test)


print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test,pos_label=1)))
print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test,pos_label=1)))
#print("Conjunto de teste -  exatidão para a classe positiva: {:.2f}".format(accuracy_score(y_test, y_pred_test)))










