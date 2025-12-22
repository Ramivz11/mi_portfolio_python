import requests
from bs4 import BeautifulSoup
import csv
import datetime # Importamos para manejar fechas

def rastrear_mercadolibre():
    url = "https://articulo.mercadolibre.com.ar/MLA-2552719886-juego-2-sillas-mesa-vidrio-exterior-balcon-terraza-jardin-_JM?searchVariation=186892103066#polycard_client=offers&deal_print_id=74d64689-a449-4165-8652-d9e70adff1d6&tracking_id=9ac8ccd0-9bf7-473c-a998-70de20cbeedd"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        respuesta = requests.get(url, headers=headers)

        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.content, 'html.parser')
            
            titulo = soup.find('h1', class_='ui-pdp-title').text.strip()
            precio_meta = soup.find('meta', itemprop='price')
            
            if precio_meta:
                precio = float(precio_meta['content'])
                
                # --- NUEVO: Obtenemos la fecha de hoy ---
                fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                print(f"Guardando datos: {fecha_hoy} |    {titulo} |     $ {precio}")
                
                # --- NUEVO: Guardamos en CSV (Excel) ---
                guardar_en_csv(fecha_hoy, titulo, precio)
                
            else:
                print("No se encontró el precio.")
        else:
            print(f"Error: {respuesta.status_code}")

    except Exception as e:
        print(f"Error: {e}")

def guardar_en_csv(fecha, titulo, precio):
    # 'a' significa APPEND (agregar al final sin borrar lo anterior)
    with open('historial_precios.csv', 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        # Escribimos una fila con los datos
        writer.writerow([fecha, titulo, precio])
        print("¡Guardado exitosamente en historial_precios.csv!")

if __name__ == "__main__":
    rastrear_mercadolibre()