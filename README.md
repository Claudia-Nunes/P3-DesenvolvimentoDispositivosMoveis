Fake News Detection API 🚀

Este projeto implementa uma API em Python com FastAPI para detectar notícias falsas usando um classificador Naive Bayes treinado em dados de exemplo.

Como usar

1️⃣ Instale as dependências:

pip install -r requirements.txt

2️⃣ Treine o modelo:

python train_model.py

3️⃣ Rode o servidor:

uvicorn app.main:app --reload

A API estará disponível em http://127.0.0.1:8000/docs (Swagger).

Endpoints

POST /api/classificar-noticia → envia o texto e obtém a classificação

GET /api/historico → lista o histórico das notícias classificadas

GET /api/status → mostra o status do modelo e quantidade de itens no histórico


Estrutura de diretórios

fake-news-api/
  app/main.py
  models/
  data/exemplo.csv
  train_model.py
  requirements.txt
  README.md

Próximos passos sugeridos

✅ Integrar LIME/SHAP para explicações visuais
✅ Ajustar para outros idiomas
✅ Empacotar via Docker
✅ Trocar para modelos mais robustos como BERT/RoBERTa


---

Projeto acadêmico — Fatec Jacareí, 2025.

