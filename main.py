from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "¡Bienvenido a Security Tech - API de Reportes!"}
