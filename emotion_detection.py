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

    # Print the response for debugging
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())

    if response.status_code == 200:
        # Access the emotions correctly
        emotion_predictions = response.json().get('emotionPredictions', [])
        if emotion_predictions:
            return emotion_predictions[0]['emotion']  # Return the first emotion
        else:
            return "No emotion predictions found."
    else:
        return f"Error: {response.status_code}, {response.text}"
