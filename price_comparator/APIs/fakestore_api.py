import requests
from .traducir import get_translated_products, translate_text
from .ordenar import ordenar_productos_por_precio

class FakeStoreAPI:
    BASE_URL = "https://fakestoreapi.com/products"


    @staticmethod
    def get_products(search_term):
        response = requests.get(FakeStoreAPI.BASE_URL)
        if response.status_code == 200:
            products_json = response.json()
            search_term = translate_text(search_term, target_lang='en')
            
            # Filtrar primero
            filtered_products = [product for product in products_json if search_term.lower() in product['title'].lower()]

            # Limitar el número de productos antes de traducir y ordenar
            limited_products = filtered_products[:5]

            # Traducir solo los productos limitados
            translated_products = [get_translated_products(product) for product in limited_products]

            # Ordenar los productos por precio
            sorted_products = sorted(translated_products, key=lambda x: x['price'])
            return sorted_products
        return []





