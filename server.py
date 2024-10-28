"""
server.py

This module serves a Flask web application that detects emotions in given text input.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Endpoint for detecting emotions from a given text.
    
    Returns:
        JSON response with detected emotions and the dominant emotion or an error message.
    """
    data = request.get_json()
    text = data.get('text', '').strip()  # Get text from request data and strip whitespace

    # Check if the text is empty
    if not text:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Call the emotion detector function
    result = emotion_detector(text)

    # Check if the dominant emotion is None
    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Prepare the response message
    response_text = f"For the given statement, the system response is " \
                    f"'anger': {result['anger']}, 'disgust': {result['disgust']}, " \
                    f"'fear': {result['fear']}, 'joy': {result['joy']} and " \
                    f"'sadness': {result['sadness']}. The dominant emotion is " \
                    f"{result['dominant_emotion']}."

    return jsonify({"message": response_text})

if __name__ == '__main__':
    app.run(debug=False)
