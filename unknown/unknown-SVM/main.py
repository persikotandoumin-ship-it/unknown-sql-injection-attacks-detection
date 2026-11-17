import string
import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report


data = {
    "query": [
        "SELECT * FROM users WHERE id=5",
        "SELECT name FROM products",
        "' OR 1=1 --",
        "admin' UNION SELECT password FROM users --",
        "DROP TABLE users; --",
        "SELECT * FROM orders WHERE order_id=10"
   
           ],
           
    "label": [0, 0, 1, 1, 1, 0]  # 0=normal, 1=SQLia
}

df = pd.DataFrame(data) 

X_train, X_test, y_train, y_test = train_test_split(
    df["query"], df["label"], test_size=0.3, random_state=42
)

# Pipeline TF-IDF + SVM
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        analyzer="char",
        ngram_range=(2, 5)
    )),
    ("svm", LinearSVC(C=1.0))
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))

# Test d'une attaque inconnue
test_query = "OR AND XOR NOT UNION DROP DELETE TRUNCATE EXEC SELECT UPDATE INSERT LIKE CONVERT() SLEEP() [!@#$%^&*()_+=\-{}[\]:;\'<>,.?/\\|`~]' "
prediction = model.predict([test_query])

if prediction[0] == 1:
    print("Unknown SQL Injection Detected")
else:
    print("Requête normale")
