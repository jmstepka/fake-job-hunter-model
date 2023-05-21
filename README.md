# fake-job-hunter-model

This is a supevised learning model component for the Fake Job Hunter app, at the Supervision Hack event.

# Environment setup

To ensure you have all of the required packages, install them in your environment by running:

```bash
pip3 install -r requirements.txt
```

# Usage

You can communicate with the model using a simple Flask API. To start a server run:

```bash
python3 -m src.server
```

If the Flask server is running, then the server from the fake-job-hunter-app repository will be able to communcate with this server.

For other uses of this API, connect to it using port 4200.

The model is trained on data located in `data/examples.csv`. You can add new examples there, and train the model by running:

```bash
python3 src/model.py
```

Model parameters are then saved in `model/model_params.joblib`

# API endpoints

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /classify | Classifies job descriptions and return probabilities that they are fake|
| POST | /retrain | Saves annotated data and retrains the model using this new information|

Body examples for endpoints:

- classify

```json
{
    "descriptions": ["description1", "description2"]
}
```

- retrain

```json
[
    {
        "description": "description1",
        "annotation": 1
    }
]
```


