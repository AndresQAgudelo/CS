from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import re

app = Flask(__name__)

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
            products_list.append({'name': nombre_producto, 'price': precio_producto, 'store': 'La Tienda en Línea'})
    else:
        print('No se pudo acceder al sitio, código de estado:', response.status_code)
    return products_list

def limpiar_precio(precio):
    # Eliminar el símbolo de moneda y otros caracteres no numéricos
    # Asumiendo que el formato es con puntos para miles y sin decimales explícitos, o con coma para decimales
    precio_limpio = re.sub(r'[^\d,]', '', precio)
    # Reemplazar comas por puntos si se usan para decimales
    precio_limpio = precio_limpio.replace(',', '.')
    # Eliminar puntos usados como separadores de miles
    precio_limpio = re.sub(r'\.(?=\d{3}(\D|$))', '', precio_limpio)
    return float(precio_limpio)

def encontrar_precio_mas_bajo(products_list):
    if not products_list:
        return None
    # Utilizar la función limpiar_precio para obtener el precio como flotante
    precio_mas_bajo = min(products_list, key=lambda x: limpiar_precio(x['price']))
    return precio_mas_bajo


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
            products_list.append({'name': nombre_producto, 'price': precio_producto, 'store': 'Mercado Libre'})
    else:
        print('No se pudo acceder al sitio, código de estado:', response.status_code)
    return products_list


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product = request.form['product']
        # Buscar productos en ambas tiendas
        products_la_tienda = obtener_datos_la_tienda_en_linea(product)
        products_mercado_libre = obtener_datos_de_mercadolibre(product)
        all_products = products_la_tienda + products_mercado_libre

        products_by_store = defaultdict(list)
        for product in all_products:
            products_by_store[product['store']].append(product)
        
        lowest_priced_product = encontrar_precio_mas_bajo(all_products)

        return render_template('results.html', products_by_store=products_by_store, lowest_priced_product=lowest_priced_product)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
