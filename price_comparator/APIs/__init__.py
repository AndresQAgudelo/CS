from .fakestore_api import FakeStoreAPI
from .dummyjson_api import DummyJSONAPI
from .la_tienda_en_linea import obtener_datos_la_tienda_en_linea
from .mercado_libre import obtener_datos_de_mercadolibre

class APIClient:
    @staticmethod
    def get_all_products(search_query):
        fakestore_products = FakeStoreAPI.get_products()
        dummyjson_products = DummyJSONAPI.get_products()
        tienda_products = obtener_datos_la_tienda_en_linea(search_query)
        mercadolibre_products = obtener_datos_de_mercadolibre(search_query)
        return fakestore_products + dummyjson_products + tienda_products + mercadolibre_products
    
