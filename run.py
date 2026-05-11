# script simple pour lancer l'app umbra d'un coup
import uvicorn
import webbrowser
import threading
import time

def ouvrir_navigateur():
    # attend 1.5 seconde que le serveur demarre et ouvre la page web
    time.sleep(1.5)
    webbrowser.open("http://localhost:8031")

if __name__ == "__main__":
    print("------------------------------------------------------------------")
    print(" 🌑  Lancement de UMBRA Market Exposure UI on port 8031")
    print(" Ouverture du navigateur sur http://localhost:8031")
    print("------------------------------------------------------------------")
    
    # ouvrir la page automatiquement
    threading.Thread(target=ouvrir_navigateur, daemon=True).start()
    
    # demarrage du serveur web fastapi
    uvicorn.run("umbra_market_exposure.api:app", host="127.0.0.1", port=8031, reload=True)
