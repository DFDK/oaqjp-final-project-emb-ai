"""Flask server for NLP Emotion Detection application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def index():
    """Render the main page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def run_sentiment_analysis():
    """Detect emotions from the given text and return a formatted response."""
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    if emotions["dominant_emotion"] == "None":
        system_response = "Invalid text! Please try again!"
    else:
        system_response = (
            f"For the given statement, the system response is "
            f"'anger': {emotions['anger']}, "
            f"'disgust': {emotions['disgust']}, "
            f"'fear': {emotions['fear']}, "
            f"'joy': {emotions['joy']} and "
            f"'sadness': {emotions['sadness']}. "
            f"The dominant emotion is {emotions['dominant_emotion']}"
        )
    return system_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
