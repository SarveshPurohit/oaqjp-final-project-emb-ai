from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    data = request.get_json()
    text = data.get('text', '').strip()  # Ensure whitespace is removed

    if not text:  # Check for empty text after stripping
        return jsonify({'message': 'Invalid text! Please try again!'}), 400

    result = emotion_detector(text)
    
    if result['dominant_emotion'] is None:
        return jsonify({'message': 'Invalid text! Please try again!'}), 400
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
