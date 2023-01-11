import pandas as pd
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

from trabalho2 import modelo, modelo2, modelo3, modelo4, modelo5, modelo6, modelo7#, modelo8, modelo9, modelo10, modelo11, modelo12

test = pd.read_csv("test.csv")
#print(test)
X_test =  test.drop('Failure',axis='columns') 
y_test =  test['Failure']
y_pred_test = modelo.predict(X_test)		# Random Forest Classifier
y_pred_test2 = modelo2.predict(X_test)		# Random Forest Regressor
y_pred_test3 = modelo3.predict(X_test)		# Extremly Randomized Trees Classifier
y_pred_test4 = modelo4.predict(X_test)		# Extremly Randomized Regressor
y_pred_test5 = modelo5.predict(X_test)		# KNN
#y_pred_test6 = modelo6.predict(X_test)		# Logistic Regression
y_pred_test7 = modelo7.predict(X_test)		# Grading Bosting Machine 
#y_pred_test8 = modelo8.predict(X_test) 		# Grading Bosting Regressor
#y_pred_test9 = modelo9.predict(X_test) 		# Naive Bayes
#y_pred_test10 = modelo10.predict(X_test) 	# Linear Regression
#y_pred_test11 = modelo11.predict(X_test) 	# SVN
#y_pred_test12 = modelo12.predict(X_test)	# Decision Tree Classifier

#print(y_pred_test5)

print("Random Forest Classifier: ")

print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test,pos_label=1)))
print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test,pos_label=1)))

print("\n########################################################################################################################\n")

print("Random Forest Regressor: ")
print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test2,pos_label=1)))
print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test2,pos_label=1)))

print("\n########################################################################################################################\n")

print("Extremly Randomized Forest Classifier: ")
print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test3,pos_label=1)))
print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test3,pos_label=1)))


print("\n########################################################################################################################\n")

print("Extremly Randomized Forest Regressor: ")
print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test4,pos_label=1)))
print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test4,pos_label=1)))


print("\n########################################################################################################################\n")

print("KNN: [OUT]")
print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test5,pos_label=1)))
print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test5,pos_label=1)))

#print("\n########################################################################################################################\n")

#print("Logistic Regression:")
#print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test6,pos_label=1)))
#print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test6,pos_label=1)))

#print("\n########################################################################################################################\n")

#print("Grading Bosting Machine :")
#print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test7,pos_label=1)))
#print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test7,pos_label=1)))

#print("\n########################################################################################################################\n")

#print("Grading Bosting Machine Regressor:")
#print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test8,pos_label=1)))
#print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test8,pos_label=1)))

#print("\n########################################################################################################################\n")

#print("Naive Bayes: [OUT]")

#print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test9,pos_label=1)))
#print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test9,pos_label=1)))

#print("\n########################################################################################################################\n")

#print("Linear Regression:")
#print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test10,pos_label=1)))
#print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test10,pos_label=1)))

#print("\n########################################################################################################################\n")

#print("SVN:")
#print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test11,pos_label=1)))
#print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test11,pos_label=1)))

#print("\n########################################################################################################################\n")

#print("Decision Tree Classifier:")
#print("Conjunto de teste - cobertura para a classe positiva: {:.2f}".format(recall_score(y_test, y_pred_test12,pos_label=1)))
#print("Conjunto de teste -  precisão para a classe positiva: {:.2f}".format(precision_score(y_test, y_pred_test12,pos_label=1)))


print("\n########################################################################################################################\n")
