import pandas as pd
column_names = ['party',
                'handicapped-infants',
                'water-project-cost-sharing',
                'adoption-of-the-budget-resolution',
                'physician-fee-freeze',
                'el-salvador-aid',
                'religious-groups-in-schools',
                'anti-satellite-test-ban',
                'aid-to-nicaraguan-contras',
                'mx-missile',
                'immigration',
                'synfuels-corporation-cutback',
                'education',
                'superfund-right-to-sue',
                'crime',
                'duty-free-exports',
                'export-administration-act-south-africa',
                ]
df = pd.read_csv('data/house-votes-84.data', header=None, names=column_names)
print(df.head())

# Counting
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure()
sns.countplot(x='education', hue='party', data=df, palette='RdBu')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()

# K Neighbors Classifier

# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
df = df[df['education'] != '?']
y = df['party'].values
X = df['education'].replace('y', True).replace('n', False).values.reshape(-1, 1)
# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
print('Fitting')
knn.fit(X, y)

# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new_data = {'education': [True, False]}
X_new = pd.DataFrame(data=new_data)['education'].values.reshape(-1, 1)
new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))