# API FastAPI pour le moteur Umbra Market Exposure
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .exposure import calculate_exposure

app = FastAPI(
    title="Umbra Market Exposure API",
    description="Moteur de Calcul d'Exposition aux Risques & Conformité",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil avec matrice de risque
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Umbra API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Umbra", "version": "1.0.0"}

@app.get("/api/v1/exposure", response_model=ResultContract)
def get_exposure(siren: str = Query("383474814")):
    return calculate_exposure(siren)
