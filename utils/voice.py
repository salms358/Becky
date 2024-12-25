import speech_recognition as sr
import pyttsx3

def listen_to_user():
    """
    Listen to the user and convert their speech to text.
    :return: Text from speech
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Sorry, my speech service is down."

def speak(text):
    """
    Convert text to speech.
    :param text: The text to speak
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
