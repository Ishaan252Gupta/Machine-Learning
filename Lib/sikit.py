from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression  # <-- New import added
from sklearn.metrics import accuracy_score

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.2,
    random_state=42
)

dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_y_pred = dt_model.predict(X_test)

dt_accuracy = accuracy_score(y_test, dt_y_pred)
print(f"Decision Tree Accuracy: {dt_accuracy * 100:.2f}%")

lr_model = LogisticRegression(max_iter=200, random_state=42)
lr_model.fit(X_train, y_train)
lr_y_pred = lr_model.predict(X_test)

lr_accuracy = accuracy_score(y_test, lr_y_pred)
print(f"Logistic Regression Accuracy: {lr_accuracy * 100:.2f}%")
import tensorflow as tf
a=tf.constant(10)
b=tf.constant(20)
c=a+b
print(c)
d=a*b
print(d)
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.preprocessing import StandardScaler

a = np.arange(1, 7).reshape(3, 2)
a = a * 10
print(a) 
b = pd.DataFrame(a, columns=["Feature_A", "Feature_B"])
print(b)
scaler = StandardScaler()
scaled = scaler.fit_transform(b)
print(scaled)

tensor = tf.constant(scaled, dtype=tf.float32)
print(tensor)

layer = tf.keras.layers.Dense(1, activation="relu")
output = layer(tensor)

print(output)