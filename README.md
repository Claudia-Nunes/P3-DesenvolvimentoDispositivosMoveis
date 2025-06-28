
# Fake News API

## Como rodar

1. Instale dependências:
```
pip install -r requirements.txt
```

2. Treine o modelo:
```
python train_model.py
```

3. Rode a API:
```
uvicorn app.main:app --reload
```

Acesse em http://127.0.0.1:8000/docs

## Endpoints
- POST /api/classificar-noticia
- GET /api/historico
- GET /api/status
