
from flask import Flask, send_from_directory, jsonify, request, render_template, abort
import os, json
BASE = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE, 'data')
PASSWORD = '1234'  # change here if needed
app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products_page():
    return render_template('products.html')

@app.route('/services')
def services_page():
    return render_template('services.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/admin')
def admin_page():
    return render_template('admin.html')

@app.route('/api/products')
def api_products():
    try:
        with open(os.path.join(DATA_DIR,'products.json'), 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    except Exception as e:
        return jsonify([])

@app.route('/api/services')
def api_services():
    try:
        with open(os.path.join(DATA_DIR,'services.json'), 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    except Exception as e:
        return jsonify([])

@app.route('/api/save', methods=['POST'])


@app.route('/api/contact')
def api_contact():
    try:
        with open(os.path.join(DATA_DIR,'contact.json'), 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    except Exception as e:
        return jsonify({})

def api_save():
    data = request.get_json(silent=True)
    if not data or 'pwd' not in data or data.get('pwd') != PASSWORD:
        abort(403)
    if 'products' in data:
        with open(os.path.join(DATA_DIR,'products.json'),'w',encoding='utf-8') as f:
            json.dump(data['products'], f, ensure_ascii=False, indent=2)
    if 'services' in data:
        with open(os.path.join(DATA_DIR,'services.json'),'w',encoding='utf-8') as f:
            json.dump(data['services'], f, ensure_ascii=False, indent=2)
    if 'contact' in data:
        with open(os.path.join(DATA_DIR,'contact.json'),'w',encoding='utf-8') as f:
            json.dump(data['contact'], f, ensure_ascii=False, indent=2)
    return 'تم الحفظ بنجاح'

if __name__ == '__main__':
    # host 0.0.0.0 so accessible on LAN, port 5000
    app.run(host='0.0.0.0', port=5000)
