from textblob import TextBlob

def analyze_emotion(text):
    """
    Analyze the emotion of a given text using TextBlob sentiment analysis.
    :param text: User input as text
    :return: Emotion as 'happy', 'sad', or 'neutral'
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # -1.0 (negative) to 1.0 (positive)
    if polarity > 0.5:
        return "happy"
    elif polarity < -0.5:
        return "sad"
    else:
        return "neutral"
