"""
This module deploys a web application for emotion detection.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/")
def render_index_page():
    """
    This function initiates the index page.
    """

    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_dect():
    """
    This function executes the emotion_detector function, receiving as input the textToAnalyze
    variable provided by the mywebscript.js.
    """

    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    displayed_response = (
        "For the given statement, the system response is: "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}"
        f"'joy': {joy_score} and 'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}"
    )

    return displayed_response

if __name__ == "__main__":
    app.run(debug=True, port=5000)