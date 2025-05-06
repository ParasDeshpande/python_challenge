#Task6: First ML model with scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#Load Dataset
iris=load_iris()
x=iris.data
y=iris.target

print("Feature shape:",x.shape)
print("Target shape:",y.shape)

#split data(80,20)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#Train model
model= RandomForestClassifier(random_state=42)
model.fit(x_train,y_train)

#Predict on test data
y_pred=model.predict(x_test)

#Accuracy
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy score:",accuracy)

#Predict new data
sample=[[5.1,3.5,1.4,0.2]]
predicted_class=model.predict(sample)
print("\nPrediction for sample:",iris.target_names[predicted_class][0])