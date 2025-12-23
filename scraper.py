import requests
from bs4 import BeautifulSoup
import csv
import datetime
import schedule # Importamos la librería de agenda
import time     # Importamos para manejar el tiempo de espera

def rastrear_mercadolibre():
    # --- Configuración ---
    url = "https://articulo.mercadolibre.com.ar/MLA-2552719886-juego-2-sillas-mesa-vidrio-exterior-balcon-terraza-jardin-_JM?searchVariation=186892103066#polycard_client=offers&deal_print_id=74d64689-a449-4165-8652-d9e70adff1d6&tracking_id=9ac8ccd0-9bf7-473c-a998-70de20cbeedd"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"--- Ejecutando escaneo: {datetime.datetime.now()} ---")

    try:
        respuesta = requests.get(url, headers=headers)
        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.content, 'html.parser')
            
            titulo = soup.find('h1', class_='ui-pdp-title').text.strip()
            precio_meta = soup.find('meta', itemprop='price')
            
            if precio_meta:
                precio = float(precio_meta['content'])
                fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                print(f"Dato encontrado: {titulo} | ${precio}")
                guardar_en_csv(fecha_hoy, titulo, precio)
            else:
                print("No se encontró el precio.")
        else:
            print(f"Error conexión: {respuesta.status_code}")
    except Exception as e:
        print(f"Error script: {e}")

def guardar_en_csv(fecha, titulo, precio):
    with open('historial_precios.csv', 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([fecha, titulo, precio])
        print(">> Guardado en CSV")

# --- BLOQUE DE AUTOMATIZACIÓN ---

def iniciar_bot():
    print("🤖 Bot de precios iniciado. Presiona Ctrl+C para detenerlo.")
    
    # 1. Programamos la tarea
    # Para testear AHORA, descomenta la línea de abajo (cada 1 minuto):
    #schedule.every(1).minutes.do(rastrear_mercadolibre)
    
    # Para el uso real (todos los días a las 10:00 am):
    schedule.every().day.at("10:00").do(rastrear_mercadolibre)
    
    # 2. Bucle Infinito 
    while True:
        # Revisa si hay alguna tarea pendiente
        schedule.run_pending()
        # Espera 1 segundo antes de volver a revisar (para no saturar tu CPU)
        time.sleep(1)

if __name__ == "__main__":
    iniciar_bot()