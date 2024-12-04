import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

data=pd.read_csv("deploy_train.csv")

X=data.drop("y",axis=1)
y=data["y"] 
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2, random_state=42)
pipe=Pipeline([("scaler",StandardScaler()),("LR",LogisticRegression())])
pipe.fit(X_train,y_train)

with open("./model.pkl", "wb") as f: 
        pickle.dump(pipe, f) 