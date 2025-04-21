import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load the data
iris = load_iris()
X, y = iris.data, iris.target

# Train a simple model
model = LogisticRegression()
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model saved as model.pkl")
import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load the data
iris = load_iris()
X, y = iris.data, iris.target

# Train a simple model
model = LogisticRegression()
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model saved as model.pkl")
