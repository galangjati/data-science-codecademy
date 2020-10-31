import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv('passengers.csv')


# Update sex column to numerical
passengers['Sex'] = passengers['Sex'].map({'female':1, 'male':0})

# Fill the nan values in the age column
passengers['Age'].fillna(np.mean(passengers['Age']), inplace=True)

# Create a first class column
passengers['FirstClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 1 else 0)

# Create a second class column
passengers['SecondClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 2 else 0)

# Select the desired features
features = passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']]
survival = passengers['Survived']

# Perform train, test, split
features_train, features_test, survival_train, survival_test = train_test_split(features, survival, test_size=.8)

# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()

features_train = scaler.fit_transform(features_train)
features_test = scaler.transform(features_test)

# Create and train the model
model = LogisticRegression()
model.fit(features_train, survival_train)

# Score the model on the train data
print(model.score(features_train, survival_train))

# Score the model on the test data
print(model.score(features_test, survival_test))

# Analyze the coefficients
print(model.coef_)

# Sample passenger features
Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
Galang = np.array([0.0,22.0,0.0,0.0])

# Combine passenger arrays
sample_passengers = np.array([Jack, Rose, Galang])

# Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)
print(sample_passengers)

# Make survival predictions!
print(model.predict_proba(sample_passengers))
