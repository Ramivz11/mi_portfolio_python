import requests
from bs4 import BeautifulSoup

def rastrear_mercadolibre():
    # 1. URL del producto 
    url = "https://articulo.mercadolibre.com.ar/MLA-2552719886-juego-2-sillas-mesa-vidrio-exterior-balcon-terraza-jardin-_JM?searchVariation=186892103066#polycard_client=offers&deal_print_id=74d64689-a449-4165-8652-d9e70adff1d6&tracking_id=9ac8ccd0-9bf7-473c-a998-70de20cbeedd"
    # 2. EL DISFRAZ (Headers)
    # Esto es crucial. Sin esto, MercadoLibre nos rechaza la conexión.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"Consultando MercadoLibre...")
    
    try:
        respuesta = requests.get(url, headers=headers)

        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.content, 'html.parser')

            # 3. EXTRACCIÓN DE DATOS
            # Buscamos el título por su clase visual
            titulo = soup.find('h1', class_='ui-pdp-title').text.strip()
            
            # TRUCO PRO: Buscamos el precio en los metadatos ocultos
            # Es más confiable que buscar los numeritos visuales
            precio_meta = soup.find('meta', itemprop='price')
            
            if precio_meta:
                precio = float(precio_meta['content']) # Lo convertimos a número
                
                # Formateamos en Pesos Argentinos (con separador de miles)
                precio_formateado = f"${precio:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
                
                print("\n--- RESULTADO MERCADOLIBRE ---")
                print(f"Producto: {titulo}")
                print(f"Precio: {precio_formateado} ARS")
                print("------------------------------")
            else:
                print("No encontré el precio. Puede que la publicación esté pausada.")
        
        else:
            print(f"Error al entrar a la página: {respuesta.status_code}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    rastrear_mercadolibre()