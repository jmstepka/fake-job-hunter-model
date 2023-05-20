import spacy
import yaml
import pandas as pd


def load_config():
    with open('src/config.yml', 'r') as f:
        config = yaml.safe_load(f)
    return config

def load_and_lemmatize_keywords():
    config = load_config()

    keywords = pd.read_csv(config["keywords_path"], header=None)
    keywords = list(keywords.iloc[:,0])

    nlp = spacy.load("pl_core_news_md")
    lemmatized_keywords = [' '.join([token.lemma_ for token in nlp(phrase)]) for phrase in keywords]

    return keywords, lemmatized_keywords

def lemmatize_description(description):
    nlp = spacy.load("pl_core_news_md")

    description_lemmatized = ' '.join([token.lemma_ for token in nlp(description)])

    return description_lemmatized

def count_keywords(keywords, lem_keywords, desc_lem):
    counts = {}

    for phrase_lem, phrase in zip(lem_keywords, keywords):
        if phrase_lem in desc_lem:
            counts[phrase] = counts.get(phrase, 0) + desc_lem.count(phrase_lem)

    return counts

def process_description(descriptions):
    keywords, lemmatized_keywords = load_and_lemmatize_keywords()
    counts = []

    for desc in descriptions:
        counts.append(count_keywords(keywords,
                                     lemmatized_keywords,
                                     lemmatize_description(desc)))

    return counts
