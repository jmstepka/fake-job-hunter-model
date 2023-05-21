from flask import Flask, request, jsonify

from src import model
from src import keyword_analysis

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
    descriptions = request.get_json().get('descriptions')
    if descriptions is None or not isinstance(descriptions, list):
        return jsonify({'error': 'Invalid input'}), 400

    predicted_classes = model.predict(descriptions)
    keyword_counts = keyword_analysis.process_description(descriptions)

    return [{'rating': pred, 'counts': counts} for pred, counts in zip(predicted_classes, keyword_counts)]

@app.route('/retrain', methods=['POST'])
def retrain():
    data = request.get_json()
    if data is None or not isinstance(data, list):
        return jsonify({'error': 'Invalid input'}), 400
    
    accuracy = model.save_new_data_and_train(data)
    return {"accuracy": accuracy}

if __name__ == '__main__':
    app.run(port=4200)