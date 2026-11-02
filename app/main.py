from fastapi import FastAPI

app = FastAPI(
    title="API de Controle de Estoque",
    description="Gerenciamento de entrada e saída de mercadorias",
    version="1.0.0"
)

@app.get("/")
def inicio():
    return {
        "mensagem": "API de Controle de Estoque funcionando!"
    }

@app.get("/health")
def health():
    return {
        "status": "online"
    }
