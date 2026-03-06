from fastapi import FastAPI

app = FastAPI
@app.get("/")
def home():
    return{"mensaje":"Mi API está funcionando"}
@app.get("/eventos")
def listar_eventos():
    return{"eventos":["Presentación Leo","Jakarta 11", "Wildfly"]}
