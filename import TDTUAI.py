import openai
import pyttsx3
import requests

# Set up OpenAI API key
openai.api_key = "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"

# Define function to generate OpenAI response
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7,
        )
        message = response.choices[0].text.strip()
        return message
    except Exception as e:
        print(f"Error: {e}")
        return "I'm sorry, I'm not able to generate a response right now."

# Define function to speak message
def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

# Main loop for chatbot
while True:
    # Prompt user for input
    prompt = input("You: ")

    # Generate response using OpenAI API
    if requests.get('https://api.openai.com/v1').status_code != 200:
        print("Error: OpenAI API is not available.")
        continue
    response = generate_response(prompt)

    # Speak out response
    speak("Malcus: " + response)

    