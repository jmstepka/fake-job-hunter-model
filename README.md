# fake-job-hunter-model

This is a supevised learning model component for the Fake Job Hunter app, at the Supervision Hack event.

# Environment setup

To ensure you have all of the required packages, install them in your environment by running:

```bash
pip3 install -r requirements.txt
```

# Usage

You can communicate with the model using a simple Flask API. To start a server run:

```python
python3 -m src.server
```

If the Flask server is running, then the server from the fake-job-hunter-app repository will be able to communcate with this server.

For other uses of this API, connect to it using port 4200.

# API endpoints

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /classify | Classifies job descriptions and return probabilities that they are fake|
| POST | /retrain | Saves annotated data and retrains the model using this new information|

Body examples for enpoints:

- classify

```json
{
    "descriptions": ["description1", "description2"]
}
```


