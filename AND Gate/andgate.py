from sklearn.linear_model import Perceptron
x_train=[[0,0],[0,1],[1,0],[1,1]]
y_train=[0,0,0,1]
clf=Perceptron(tol=3,random_state=0)
clf.fit(x_train,y_train)
x_test=[[1,1],[0,0],[1,1],[0,1]]
y_predict=clf.predict(x_test)
print(y_predict)
print(clf.coef_,clf.intercept_)
print(clf.score(x_test,y_predict))