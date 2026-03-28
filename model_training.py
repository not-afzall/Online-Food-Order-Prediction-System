import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

# Load dataset
df = pd.read_csv("food_order_data.csv")

# Encode categorical variables
le_gender = LabelEncoder()
le_location = LabelEncoder()
le_target = LabelEncoder()

df['Gender'] = le_gender.fit_transform(df['Gender'])
df['Location'] = le_location.fit_transform(df['Location'])
df['Ordered'] = le_target.fit_transform(df['Ordered'])

# Features and target
X = df[['Age', 'Gender', 'Location', 'Income', 'Order_History']]
y = df['Ordered']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save encoders
with open("encoders.pkl", "wb") as f:
    pickle.dump((le_gender, le_location, le_target), f)

print("Model and encoders saved!")