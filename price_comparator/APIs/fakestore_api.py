import requests

class FakeStoreAPI:
    BASE_URL = "https://fakestoreapi.com/products"
    
    @staticmethod
    def get_products():
        response = requests.get(FakeStoreAPI.BASE_URL)
        if response.status_code == 200:
            return response.json()
        return []
