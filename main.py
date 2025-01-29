from utils.emotions import analyze_emotion
from utils.weather import get_weather
from utils.voice import listen_to_user, speak


# Empathetic response function
def empathetic_response(emotion, user_input):
    if "depressed" in user_input.lower() or "sad" in user_input.lower():
        return [
            "I'm really sorry to hear that. 😔 You're not alone, and it's okay to feel this way.",
            "Would you like me to share something uplifting? Maybe a motivational quote or a calming exercise?",
            "If you need someone to talk to, I can help you find a helpline or resource nearby."
        ]
    elif "happy" in emotion:
        return [
            "That's wonderful to hear! 🌟 Want to celebrate with a joke or fun fact?",
            "Happiness looks good on you! Keep shining!"
        ]
    elif "neutral" in emotion:
        return [
            "Got it. Is there anything you'd like to talk about?",
            "I'm here if you need me—let me know how I can assist!"
        ]
    else:
        return ["I'm here for you. Let me know how I can help. 💙"]


# Main function
def main():
    print("Hi, I'm Becky, your personal assistant!")
    while True:
        # Get user input (can be replaced with voice input)
        user_input = input("You: ")

        # Exit command
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Becky: Goodbye! Have a great day!")
            # speak("Goodbye! Have a great day!")  # Uncomment if voice enabled
            break

        # Emotion analysis
        emotion = analyze_emotion(user_input)

        # Get empathetic response
        responses = empathetic_response(emotion, user_input)

        # Display all responses (for sad/emotional cases)
        for response in responses:
            print(f"Becky: {response}")

        # Offer actions based on emotion
        if "depressed" in user_input.lower() or "sad" in user_input.lower():
            action = input("Becky: Would you like a motivational quote or a calming exercise? (quote/exercise) ")
            if action.lower() == "quote":
                print("Becky: Here's something to lift your spirits:")
                print(f"Becky: {get_motivational_quote()}")
            elif action.lower() == "exercise":
                print("Becky: Let’s try a calming exercise together:")
                for step in calming_exercise():
                    print(f"Becky: {step}")
            else:
                print("Becky: That's okay. I'm here if you need me. 💙")

        # Weather functionality example
        if "weather" in user_input.lower():
            city = input("Which city? ")
            weather_response = get_weather(city)
            print(f"Becky: {weather_response}")
            # speak(weather_response)  # Uncomment for voice


# Motivational quote function
def get_motivational_quote():
    quotes = [
        "You are stronger than you think. Keep pushing forward. 💪",
        "Every day may not be good, but there is something good in every day. 🌟",
        "You’ve survived 100% of your worst days. You’re amazing. Keep going. 🌈",
        "Your mental health is important. Take it one step at a time. 💙"
    ]
    import random
    return random.choice(quotes)


# Calming exercise function
def calming_exercise():
    return [
        "Breathe in slowly for 4 seconds...",
        "Hold your breath for 4 seconds...",
        "Now exhale slowly for 4 seconds. Repeat this a few times. You’ve got this. 💙"
    ]


if __name__ == "__main__":
    main()

