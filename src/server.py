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
    print(list(keyword_counts[0].keys()))
    # return jsonify([{'rating': pred, 'counts': counts} for pred, counts in zip(predicted_classes, keyword_counts)])
    return [{'rating': pred, 'counts': counts} for pred, counts in zip(predicted_classes, keyword_counts)]

if __name__ == '__main__':
    app.run(port=3000)