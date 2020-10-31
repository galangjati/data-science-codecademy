import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

breast_cancer_data = load_breast_cancer()

#print(breast_cancer_data.data[0])
#print(breast_cancer_data.feature_names)
#print(breast_cancer_data.target)
#print(breast_cancer_data.target_names)

train_data, val_data, train_labels, val_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 1000)

#print(len(train_data))
#print(len(train_labels))
accuracies = []

for k in range(1, 101):
  classifier = KNeighborsClassifier(k)
  classifier.fit(train_data, train_labels)
  accuracies.append(classifier.score(val_data, val_labels))

k_list = range(1, 101)
plt.plot(k_list, accuracies)
plt.xlabel('k')
plt.ylabel('Val Accuracy')
plt.title('Breast Cancer Classifier Accuracy')
plt.show()