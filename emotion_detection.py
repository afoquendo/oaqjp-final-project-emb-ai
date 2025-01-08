"""
This module defines a function to call the Emotion Predict API from the watson NLP Library
"""
import requests
import json

def emotion_detector(text_to_analyse):
    """
    Returns the response of the Emotion Predict function of the watson NLP Library for the
    string text_to_analyse.

    Args:
        text_to_analyse (str): Text to be analyzed by emotion Predict.
    
    Returns:
        str: Text that contains the response from the API.

    """

    url = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/'
           'EmotionPredict')
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    formatted_response = json.loads(response.text)
    scores = formatted_response['emotionPredictions'][0]['emotion']
    scores['dominant_emotion'] = max(scores, key=scores.get)
    return scores
