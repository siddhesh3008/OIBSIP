
#Define Main Function and Voice Command Parsing

from assistant import speak, listen, get_time, get_date, search_wikipedia, get_weather, send_email

def process_command(command):
    if "time" in command:
        get_time()
    elif "date" in command:
        get_date()
    elif "search wikipedia" in command:
        speak("What do you want to search on Wikipedia?")
        query = listen()
        search_wikipedia(query)
    elif "weather" in command:
        speak("Please provide the city name.")
        city = listen()
        get_weather(city)
    elif "send email" in command:
        speak("What should be the subject?")
        subject = listen()
        speak("What should be the message?")
        message = listen()
        send_email("recipient@example.com", subject, message)
    else:
        speak("Sorry, I didn't understand that command.")

def main():
    speak("Hello! How can I assist you?")
    while True:
        command = listen()
        process_command(command)

if __name__ == "__main__":
    main()
