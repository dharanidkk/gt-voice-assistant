from datetime import datetime
import webbrowser
import urllib.parse

import pyttsx3

try:
    import speech_recognition as sr
except ImportError:
    sr = None


class GTVoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 170)

    def speak(self, message):
        print(f"Assistant: {message}")
        self.engine.say(message)
        self.engine.runAndWait()

    def listen(self):
        if sr is None:
            self.speak("Speech recognition is not installed. Please use text mode.")
            return ""

        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening... Speak now.")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            print("Recognizing speech...")
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            self.speak("I did not hear anything. Please try again.")
        except sr.UnknownValueError:
            self.speak("Sorry, I could not understand that.")
        except sr.RequestError:
            self.speak("Speech recognition service is unavailable. Check your internet connection.")
        except (OSError, AttributeError) as exc:
            self.speak("I could not access the microphone. You can restart and choose text mode.")
            print(f"Microphone detail: {exc}")
        return ""

    def handle_command(self, command):
        command = command.strip()
        normalized = command.lower()

        if not normalized:
            return True

        if normalized in {"exit", "quit", "stop", "goodbye"}:
            self.speak("Goodbye! Have a nice day.")
            return False

        if normalized in {"help", "commands"}:
            self.speak(
                "You can say: search followed by a topic, open YouTube, open Google, "
                "what time is it, what is today's date, or exit."
            )
            return True

        if "time" in normalized:
            self.speak("The time is " + datetime.now().strftime("%I:%M %p"))
            return True

        if "date" in normalized or "today" in normalized:
            self.speak("Today's date is " + datetime.now().strftime("%d %B %Y"))
            return True

        if "open youtube" in normalized:
            webbrowser.open("https://www.youtube.com")
            self.speak("Opening YouTube.")
            return True

        if "open google" in normalized:
            webbrowser.open("https://www.google.com")
            self.speak("Opening Google.")
            return True

        if normalized.startswith("search "):
            query = command[7:].strip()
            if query:
                url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
                webbrowser.open(url)
                self.speak("I opened search results for " + query)
            else:
                self.speak("Please say what you want to search for.")
            return True

        self.speak("I do not know that command yet. Say help to hear the available commands.")
        return True


def run_assistant(use_voice=True):
    assistant = GTVoiceAssistant()
    assistant.speak("Hello! I am GT Voice Assistant. Say help to hear available commands.")

    while True:
        try:
            if use_voice:
                command = assistant.listen()
                # An empty recognition result should not stop the assistant.
                if not command:
                    continue
            else:
                command = input("You: ")

            if not assistant.handle_command(command):
                break
        except KeyboardInterrupt:
            assistant.speak("Goodbye!")
            break
