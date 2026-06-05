import requests
import json

def emotion_detector(text_to_analyze: str):
    """function to detect emotion"""
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers=header)
    if response.status_code != "200":
        emotion = {
            "anger": "None", 
            "disgust": "None", 
            "fear": "None", 
            "joy": "None", 
            "sadness": "None", 
            "dominant_emotion":"None"
        }
    else:
        formatted_response = json.loads(response.text)
        emotion = formatted_response["emotionPredictions"][0]["emotion"]
        emotion["dominant_emotion"] = max(emotion, key=emotion.get)
    return emotion
