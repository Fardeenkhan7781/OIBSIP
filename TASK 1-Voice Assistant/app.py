import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    speak("Hello! How can I assist you today?")

def get_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return ""

def respond(command):
    if "hello" in command:
        speak("Hi there!")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
        print("Time:", current_time)
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}")
        print("Date:", current_date)
    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        speak("Searching the web for " + query)
        webbrowser.open(url)
    elif "quit" in command or "exit" in command:
        speak("Goodbye!")
        quit()
    else:
        speak("I'm sorry, I didn't understand that command.")
    print("Command:", command)

def main():
    greet()
    while True:
        command = get_command()
        respond(command)

if __name__ == "__main__":
    main()
