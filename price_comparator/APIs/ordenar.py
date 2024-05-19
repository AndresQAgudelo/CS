import re


def clean_price(price):
    # Eliminar caracteres no numéricos excepto puntos y comas
    cleaned_price = re.sub(r'[^\d.,]', '', price)
    # Reemplazar comas por puntos para el formato decimal
    cleaned_price = cleaned_price.replace(',', '.')
    # Eliminar puntos que actúan como separadores de miles
    cleaned_price = cleaned_price.replace('.', '')
    # Convertir el precio limpio a un valor flotante
    return float(cleaned_price)



def ordenar_productos_por_precio(productos):
    productos_ordenados = sorted(productos, key=lambda item: clean_price(item['price']))
    return productos_ordenados
