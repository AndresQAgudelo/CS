import requests
from bs4 import BeautifulSoup

def obtener_datos_de_mercadolibre(product):
    url = f'https://listado.mercadolibre.com.co/{product}#D[A:{product}]'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    products_list = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('li', class_='ui-search-layout__item')
        
        for item in items:
            nombre_producto = item.find('h2', class_='ui-search-item__title').text.strip() if item.find('h2', class_='ui-search-item__title') else 'No disponible'
            precio_producto = item.find('span', class_='andes-money-amount__fraction').text.strip() if item.find('span', class_='andes-money-amount__fraction') else 'No disponible'
            products_list.append({'title': nombre_producto, 'price': precio_producto, 'store': 'Mercado Libre'})
    else:
        print('No se pudo acceder al sitio, código de estado:', response.status_code)
    return products_list
