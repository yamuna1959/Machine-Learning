from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
x=[1],[2],[3],[4],[5],[6],[7],[8],[9]
y=1,4,9,16,25,36,49,64,81
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)
print(x_test)
print(knn.predict(x_test))
print(knn.score(x_test,y_test))