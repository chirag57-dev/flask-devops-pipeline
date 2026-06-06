from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])

def health_check():
    return jsonify({'status': 'ok'}),200



@app.route('/items', methods=['GET'])

def items():
        return jsonify({'items': ['item1', 'item2', 'item3']}),200
    
@app.route('/items', methods=['POST'])
def create_item():
        data = request.get_json(silent =True)
        if data is None:
            return jsonify({'message': 'Invalid data'}),400
        return jsonify({'message': 'Item created', 'data': data}),201
    
    
if __name__ == '__main__':
    app.run(debug=True)
