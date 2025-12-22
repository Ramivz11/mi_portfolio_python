import requests
from bs4 import BeautifulSoup

def rastrear_precio():
    # 1. La URL del producto que queremos rastrear
    # Usamos esta web de prueba segura
    url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

    # 2. Hacemos la petición (El "Viaje")
    print(f"Consultando {url}...")
    respuesta = requests.get(url)

    # Verificamos si la página respondió bien (Código 200)
    if respuesta.status_code == 200:
        # 3. Analizamos el contenido (El "Mapa")
        soup = BeautifulSoup(respuesta.content, 'html.parser')

        # 4. Buscamos los datos específicos
        # En esta web, el título es un <h1> y el precio tiene la clase 'price_color'
        titulo = soup.find('h1').text
        precio = soup.find('p', class_='price_color').text

        print("\n--- RESULTADO ---")
        print(f"Producto: {titulo}")
        print(f"Precio actual: {precio}")
        print("-----------------")
    else:
        print("Hubo un error al conectar con la página.")

# Ejecutamos la función
if __name__ == "__main__":
    rastrear_precio()