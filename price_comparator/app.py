from flask import Flask, render_template, request
from APIs import APIClient

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    search_query = request.form.get('search', '')
    all_products = []

    if search_query:
        all_products = APIClient.get_all_products(search_query)

    return render_template('index.html', products=all_products, search_query=search_query)

if __name__ == '__main__':
    app.run(debug=True)
