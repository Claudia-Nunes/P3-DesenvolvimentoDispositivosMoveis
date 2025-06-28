
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import os
from typing import List

app = FastAPI(title="Fake News Detection API")

model_path = os.path.join("models", "fake_news_model.pkl")
vectorizer_path = os.path.join("models", "vectorizer.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

history = []

class NewsItem(BaseModel):
    texto: str

class ClassificationResult(BaseModel):
    classe: str
    probabilidade: float
    palavras_influentes: List[str]

@app.post("/api/classificar-noticia", response_model=ClassificationResult)
def classificar_noticia(item: NewsItem):
    if not item.texto:
        raise HTTPException(status_code=400, detail="Texto vazio")
    X = vectorizer.transform([item.texto])
    prob = model.predict_proba(X)[0]
    pred = model.predict(X)[0]
    classe = "verdadeira" if pred == 1 else "falsa"
    probabilidade = float(max(prob))
    palavras = [w for w in item.texto.split()[:3]]
    resultado = ClassificationResult(
        classe=classe,
        probabilidade=probabilidade,
        palavras_influentes=palavras
    )
    history.append({"texto": item.texto, "classe": classe, "probabilidade": probabilidade})
    return resultado

@app.get("/api/historico")
def get_historico():
    return history

@app.get("/api/status")
def get_status():
    return {"status": "ok", "modelo": "NaiveBayes", "historico_itens": len(history)}
