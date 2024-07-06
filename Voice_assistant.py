import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(message):
    """Convert text to speech."""
    tts_engine.say(message)
    tts_engine.runAndWait()

def listen():
    """Capture audio from the microphone and recognize speech."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return listen()
    except sr.RequestError:
        speak("Sorry, my speech service is unavailable.")
        return ""

def tell_time():
    """Tell the current time."""
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def search_wikipedia(query):
    """Search Wikipedia for a given query and read the summary."""
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia, {summary}")
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple entries for this topic. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find any information on that topic.")
    except Exception as e:
        speak("Sorry, an error occurred while searching Wikipedia.")
        print(e)

def perform_calculation(expression):
    """Perform a basic arithmetic calculation."""
    try:
        result = eval(expression)
        speak(f"The result is {result}")
    except:
        speak("Sorry, I couldn't perform the calculation. Please try again.")

def main():
    """Main function to run the voice assistant."""
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if "time" in command:
            tell_time()
        elif "wikipedia" in command:
            speak("What would you like to search on Wikipedia?")
            query = listen()
            if query:
                search_wikipedia(query)
        elif "calculate" in command:
            speak("What calculation would you like to perform?")
            expression = listen()
            if expression:
                perform_calculation(expression)import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(message):
    """Convert text to speech."""
    tts_engine.say(message)
    tts_engine.runAndWait()

def listen():
    """
    Capture audio from the microphone and recognize speech.
    Returns the recognized text in lowercase.
    """
    with sr.Microphone() as source:
        # Adjust for ambient noise to improve recognition accuracy
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        # Recognize speech using Google Web Speech API
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        # Handle unrecognized speech
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return listen()
    except sr.RequestError:
        # Handle request errors
        speak("Sorry, my speech service is unavailable.")
        return ""

def tell_time():
    """
    Tell the current time.
    Uses the datetime library to get the current time and converts it to a string.
    """
    now = datetime.datetime.now()
    current time = now.strftime("%I:%M %p")
    speak(f"The current time is {current time}")

def search_wikipedia(query):
    """
    Search Wikipedia for a given query and read the summary.
    Handles disambiguation and page errors.
    """
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(f"According to Wikipedia, {summary}")
    except wikipedia.exceptions.DisambiguationError:
        # Handle disambiguation errors
        speak("There are multiple entries for this topic. Please be more specific.")
    except wikipedia.exceptions.PageError:
        # Handle page not found errors
        speak("I couldn't find any information on that topic.")
    except Exception as e:
        # Handle other exceptions
        speak("Sorry, an error occurred while searching Wikipedia.")
        print(e)

def perform_calculation(expression):
    """
    Perform a basic arithmetic calculation.
    Uses the eval function to evaluate the expression.
    """
    try:
        result = eval(expression)
        speak(f"The result is {result}")
    except:
        # Handle evaluation errors
        speak("Sorry, I couldn't perform the calculation. Please try again.")

def main():
    """
    Main function to run the voice assistant.
    Continuously listens for commands and performs actions accordingly.
    """
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if "time" in command:
            tell_time()
        elif "wikipedia" in command:
            speak("What would you like to search on Wikipedia?")
            query = listen()
            if query:
                search_wikipedia(query)
        elif "calculate" in command:
            speak("What calculation would you like to perform?")
            expression = listen()
            if expression:
                perform_calculation(expression)
        elif "stop" in command or "exit" in command or "bye" in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    main()
 write comments as a human not as a llm model

        elif "stop" in command or "exit" in command or "bye" in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    main()
