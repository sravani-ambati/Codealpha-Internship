# Importing necessary libraries
import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore
import webbrowser
import datetime
from tkinter import *
from PIL import Image, ImageTk # type: ignore

# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user based on the time of day
def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greeting = "Good Morning!"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    speak(f'Hello, {greeting} I am your voice assistant. Please tell me how may I help you.')

# Function to take voice command from the user
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"User said: {command}")
            return command
    except Exception as e:
        print(e)
        return None

# Function to handle commands
def handle_command(command):
    if 'who are you' in command:
        speak('I am your personal voice assistant.')

    elif 'what can you do' in command:
        speak('I can play songs, tell the time, and help you with web searches.')

    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'The current time is {current_time}.')

    elif 'google' in command:
        speak('Opening Google.')
        webbrowser.open('https://www.google.com')

    elif 'youtube' in command:
        speak('Opening YouTube.')
        webbrowser.open('https://www.youtube.com')

    elif 'facebook' in command:
        speak('Opening Facebook.')
        webbrowser.open('https://www.facebook.com')

    elif 'shutdown' in command:
        speak('Shutting down. Goodbye!')
        close_window()
        return False
    else:
        speak('I did not understand that. Could you please repeat?')
    return True

# Function to close the application window
def close_window():
    root.destroy()

# GUI Class for the voice assistant
class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        self.bg = ImageTk.PhotoImage(file="Images/white.jpeg")
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0)

        self.icon = ImageTk.PhotoImage(file="Images/voiceassistant.jpeg")
        icon_label = Label(self.root, image=self.icon)
        icon_label.place(x=100, y=100, width=400, height=400)

        start_button = Button(self.root, text='START', font=("times new roman", 14), command=self.start_assistant)
        start_button.place(x=150, y=520)

        close_button = Button(self.root, text='CLOSE', font=("times new roman", 14), command=close_window)
        close_button.place(x=350, y=520)

    def start_assistant(self):
        greet_user()
        running = True
        while running:
            command = take_command()
            if command:
                running = handle_command(command)

# Create Tkinter window
root = Tk()

# Create an object for the VoiceAssistantGUI class
assistant_gui = VoiceAssistantGUI(root)

# Start the GUI event loop
root.mainloop()
