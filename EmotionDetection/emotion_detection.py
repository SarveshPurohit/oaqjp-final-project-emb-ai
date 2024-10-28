import requests

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        # Convert response to a dictionary
        response_data = response.json()

        # Extract emotion scores
        emotion_scores = response_data['emotionPredictions'][0]['emotion']
        anger_score = emotion_scores.get('anger', 0)
        disgust_score = emotion_scores.get('disgust', 0)
        fear_score = emotion_scores.get('fear', 0)
        joy_score = emotion_scores.get('joy', 0)
        sadness_score = emotion_scores.get('sadness', 0)

        # Determine the dominant emotion
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotions, key=emotions.get)

        # Format output
        formatted_output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
        return formatted_output
    else:
        return f"Error: {response.status_code}, {response.text}"
