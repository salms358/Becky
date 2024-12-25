from utils.emotions import analyze_emotion
from utils.weather import get_weather
from utils.voice import listen_to_user, speak

def main():
    print("Hi, I'm Becky, your personal assistant!")
    while True:
        user_input = input("You: ")  # Replace with listen_to_user() if using voice
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Becky: Goodbye! Have a great day!")
            # speak("Goodbye! Have a great day!")  # Uncomment if voice enabled
            break
        
        # Emotion analysis
        emotion = analyze_emotion(user_input)
        if emotion == "happy":
            print("Becky: I'm glad you're happy! 😊")
        elif emotion == "sad":
            print("Becky: I'm sorry to hear that. I'm here for you. 😟")
        else:
            print("Becky: Got it. Let me know how I can assist!")

        # Weather functionality example
        if "weather" in user_input.lower():
            city = input("Which city? ")
            weather_response = get_weather(city)
            print(f"Becky: {weather_response}")
            # speak(weather_response)  # Uncomment for voice

if __name__ == "__main__":
    main()
