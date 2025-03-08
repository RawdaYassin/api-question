from flask import Flask, request, jsonify

app = Flask(__name__)

items = []

@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    if 'item' not in data:
        return jsonify({'error': 'Item field is required'}), 400
    items.append(data['item'])
    return jsonify({'message': 'Item added', 'items': items}), 201

@app.route('/items/<item_name>', methods=['DELETE'])
def delete_item(item_name):
    if item_name in items:
        items.remove(item_name)
        return jsonify({'message': 'Item deleted', 'items': items}), 200
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
