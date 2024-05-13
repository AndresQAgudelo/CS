import requests
from bs4 import BeautifulSoup

def obtener_datos_de_mercadolibre(product):
    # Adaptación del URL para búsqueda en Mercado Libre
    url = f'https://listado.mercadolibre.com.co/{product}#D[A:{product}]'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Adaptación de los selectores según la estructura de Mercado Libre
        items = soup.find_all('li', class_='ui-search-layout__item')  # Ajustar el selector de acuerdo a la estructura de la página
        
        for item in items:
            # Adapta estos selectores según la página de resultados de Mercado Libre
            nombre_producto = item.find('h2', class_='ui-search-item__title').text.strip() if item.find('h2', class_='ui-search-item__title') else 'No disponible'
            precio_producto = item.find('span', class_='andes-money-amount__fraction').text.strip() if item.find('span', class_='andes-money-amount__fraction') else 'No disponible'
            print(f'Producto: {nombre_producto}, Precio: {precio_producto}')
    else:
        print('No se pudo acceder al sitio, código de estado:', response.status_code)

# Pedir al usuario que ingrese el término de búsqueda
producto = input("Ingrese el término de búsqueda: ")
obtener_datos_de_mercadolibre(producto)
