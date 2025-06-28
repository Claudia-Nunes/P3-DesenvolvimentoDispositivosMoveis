
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

df = pd.read_csv("data/exemplo.csv")
X_train = df['texto']
y_train = df['label']

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_vec, y_train)

with open("models/fake_news_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("models/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Modelo treinado e salvo!")
