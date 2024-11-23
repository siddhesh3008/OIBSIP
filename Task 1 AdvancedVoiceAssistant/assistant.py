
#Initialize Speech Recognition and Text-to-Speech

import speech_recognition as sr
import pyttsx3 
import datetime
import wikipedia 
import requests 
import pywhatkit 

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        return query.lower()
    
# Create Task Functions
# Date and Time Functionality

def get_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time}")

def get_date():
    date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today is {date}")

# Wikipedia Search Functionality
def search_wikipedia(query):
    speak("Searching Wikipedia...")
    results = wikipedia.summary(query, sentences=2)
    speak(results)

# Weather API Functionality

import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp}°C with {description}")
    else:
        speak("Sorry, I couldn't retrieve the weather information.")

#Implement Email Functionality 

import smtplib

def send_email(to_email, subject, message):
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("EMAIL_PASSWORD")
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(EMAIL, to_email, email_message)
    speak("Email has been sent successfully.")
