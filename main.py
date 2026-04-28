from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API funcionando 🚀"}

@app.get("/usuario/{id}")
def get_usuario(id: int):
    return {"usuario_id": id}