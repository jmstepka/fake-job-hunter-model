from flask import Flask, request, jsonify

from src import model

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
    descriptions = request.get_json().get('descriptions')
    if descriptions is None or not isinstance(descriptions, list):
        return jsonify({'error': 'Invalid input'}), 400

    predicted_classes = model.predict(descriptions)
    return jsonify({'predicted_classes': predicted_classes})

if __name__ == '__main__':
    app.run(port=3000)