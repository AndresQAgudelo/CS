import requests

class DummyJSONAPI:
    BASE_URL = "https://dummyjson.com/products"
    
    @staticmethod
    def get_products():
        response = requests.get(DummyJSONAPI.BASE_URL)
        if response.status_code == 200:
            return response.json().get('products', [])
        return []
