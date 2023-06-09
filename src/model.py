import numpy as np
import pandas as pd
import spacy
import logging
import yaml

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score

import joblib

def load_config():
    with open('src/config.yml', 'r') as f:
        config = yaml.safe_load(f)
    return config


def load_data(path):
    data = pd.read_csv(path, sep='|')
    return data

def prepare_data_for_training(data):
    nlp = spacy.load('pl_core_news_md')
    
    data['vector'] = data['description'].apply(lambda d: nlp(d).vector)

    X, y = np.stack(data['vector'].to_numpy()), data['label']
    return X, y

def report_accuracy(X, y, clf, cv_num=5):
    
    score = cross_val_score(clf, X, y, cv=cv_num)

    print(score)
    return np.mean(score)

def load_data_examples(annotated):
    config = load_config()

    data = load_data(config['data_path'])
    if annotated:
        annotated_data = load_data(config['annotated_data_path'])

        data = pd.concat([data, annotated_data])

    return data

def create_and_save_model(annotated=False):
    config = load_config()

    data = load_data_examples(annotated)
    X, y = prepare_data_for_training(data)

    classifier = make_pipeline(MinMaxScaler(),
                               LogisticRegression())

    accuracy = report_accuracy(X, y, classifier)

    classifier.fit(X, y)

    joblib.dump(classifier, config['model_path'])
    return accuracy

def prepare_data_for_prediction(descriptions):
    nlp = spacy.load('pl_core_news_md')

    vectors = np.array([nlp(desc).vector for desc in descriptions])
    
    return vectors


def predict(descriptions):
    config = load_config()

    data = prepare_data_for_prediction(descriptions)

    model = joblib.load(config['model_path'])

    predictions = model.predict_proba(data)
    return [float(pred[1]) for pred in predictions]

def save_annotated_data(data):
    config = load_config()

    descriptions = [item['description'] for item in data]
    annotations = [item['annotation'] for item in data]

    df = pd.DataFrame({'description': descriptions, 'label': annotations})

    df.to_csv(config['annotated_data_path'], sep='|', index=False)

def save_new_data_and_train(data):
    save_annotated_data(data)

    return create_and_save_model(annotated=True)


if __name__ == "__main__":
    create_and_save_model()



