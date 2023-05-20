import numpy as np
import pandas as pd
import spacy
import logging
import yaml

from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score

from joblib import dump, load

def load_config():
    with open('src/config.yml', 'r') as f:
        config = yaml.safe_load(f)
    print(config)
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

    logging.info(f'CrossVal accuracy score: {score}')


def create_and_save_model():
    config = load_config()

    data = load_data(config['data_path'])
    X, y = prepare_data_for_training(data)

    classifier = make_pipeline(MinMaxScaler(),
                               MultinomialNB())

    report_accuracy(X, y, classifier)

    classifier.fit(X, y)

    dump(classifier, config['model_path'])

#def prepare_data_for_prediction(descriptions)

#def predict(descriptions):

if __name__ == "__main__":
    create_and_save_model()



