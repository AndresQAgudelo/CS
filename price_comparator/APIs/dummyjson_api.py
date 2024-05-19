import requests
from .traducir import get_translated_products, translate_text


class DummyJSONAPI:
    
    @staticmethod
    def get_products(search_term):
        search_term = translate_text(search_term, target_lang='en')
        BASE_URL = f"https://dummyjson.com/products/search?q={search_term}"
        response = requests.get(BASE_URL)
        
        if response.status_code == 200:
            products_json = response.json()
            if 'products' in products_json:
                products = products_json['products']
                
                # Filtrar primero antes de traducir
                filtered_products = [product for product in products if search_term.lower() in product['title'].lower()]
                
                # Limitar el número de productos antes de traducir y ordenar
                limited_products = filtered_products[:5]

                # Traducir solo los productos limitados
                translated_products = [get_translated_products(product) for product in limited_products]
                # Traducir solo los productos filtrados
                #translated_products = [get_translated_products(product) for product in filtered_products]

                # Ordenar la lista de productos por precio de menor a mayor
                sorted_products = sorted(translated_products, key=lambda x: x['price'])
                return sorted_products
            else:
                print("La respuesta JSON no contiene la clave 'products'")
        else:
            print(f"Error fetching products, status code: {response.status_code}")
        return []

