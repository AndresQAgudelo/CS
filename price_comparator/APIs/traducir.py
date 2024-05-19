from deep_translator import GoogleTranslator

translations_cache = {}  # Diccionario para almacenar traducciones y evitar llamadas repetidas

def translate_text(text, target_lang='es'):
    if text in translations_cache:
        return translations_cache[text]
    translated_text = GoogleTranslator(source='auto', target=target_lang).translate(text)
    translations_cache[text] = translated_text
    return translated_text

def get_translated_products(product):
    translated_title = translate_text(product['title'])
    translated_description = translate_text(product['description'])

    translated_product = {
        'title': translated_title,
        'description': translated_description,
        'price': product['price'],
        'store': 'fake_store',
    }
    if 'image' in product:
        translated_product['image'] = product['image']
    return translated_product
