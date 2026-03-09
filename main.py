from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def get_root():
    data = {
        "message": "Pruebas unitarias"
    }
    return JSONResponse(status_code=200, content=data)

@app.post("/sumas")
def sumar(numero1: int = 5, numero2: int = 10):
    suma = numero1 + numero2
    data = {
        "numero1": numero1,
        "numero2": numero2,
        "suma": suma
    }
    return JSONResponse(status_code=200, content=data)