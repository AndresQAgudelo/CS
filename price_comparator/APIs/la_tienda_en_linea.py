import requests
from bs4 import BeautifulSoup

def obtener_datos_la_tienda_en_linea(product):
    url = 'https://latiendaenlinea.net/index.php?controller=search&s=' + product
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    products_list = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', class_='product')  # Ajusta este selector según el sitio
        
        for item in items:
            nombre_producto = item.find('h2', class_='h3 product-title').text.strip() if item.find('h2', class_='h3 product-title') else 'No disponible'
            precio_producto = item.find('span', class_='price').text.strip() if item.find('span', class_='price') else 'No disponible'
            products_list.append({'title': nombre_producto, 'price': precio_producto, 'store': 'La Tienda en Línea'})
    else:
        print('No se pudo acceder al sitio, código de estado:', response.status_code)
    return products_list
