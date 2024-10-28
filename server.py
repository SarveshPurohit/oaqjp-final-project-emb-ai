from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    # Get the emotion detection result
    result = emotion_detector(text_to_analyze)

    # Prepare the response
    if result:
        response = {
            "anger": result['anger'],
            "disgust": result['disgust'],
            "fear": result['fear'],
            "joy": result['joy'],
            "sadness": result['sadness'],
            "dominant_emotion": result['dominant_emotion']
        }

        # Format the output message
        output_message = f"For the given statement, the system response is " \
                         f"'anger': {response['anger']}, 'disgust': {response['disgust']}, " \
                         f"'fear': {response['fear']}, 'joy': {response['joy']} and " \
                         f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
        
        return jsonify(response), 200

    return jsonify({"error": "No result found"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

