import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

def svm(dataset):

  dataset['type'] = dataset['type'].map({'S':1, 'B':0})
  dataset = dataset.dropna(subset = ['plate_x', 'plate_z', 'type'])

  fig, ax = plt.subplots()
  plt.scatter(dataset.plate_x, dataset.plate_z, c=dataset.type, cmap=plt.cm.coolwarm, alpha=0.25)

  training_set, validation_set = train_test_split(dataset, random_state=1)

  training_data = training_set[['plate_x','plate_z']]
  training_labels = training_set['type']

  classifier =SVC(kernel='rbf', gamma=3, C=1)
  classifier.fit(training_data, training_labels)
  draw_boundary(ax, classifier)
  ax.set_ylim(-2,6)
  ax.set_xlim(-3,3)
  plt.show()
  
  print(classifier.score(validation_set[['plate_x', 'plate_z']], validation_set.type))

svm(jose_altuve)