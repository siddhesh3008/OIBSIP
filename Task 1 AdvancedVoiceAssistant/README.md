Advanced Voice Assistant in Python
A Python-based voice assistant capable of handling various tasks such as fetching the current time and date, retrieving weather updates, searching Wikipedia, and sending emails. This project demonstrates the integration of Speech Recognition, Natural Language Processing (NLP), and API-based task automation.

Features
Speech Recognition: Converts spoken words into text.
Text-to-Speech (TTS): Provides audio feedback using pyttsx3.
Wikipedia Search: Retrieves concise summaries from Wikipedia.
Weather Updates: Fetches real-time weather data using OpenWeather API.
Email Functionality: Sends emails through Gmail with the SMTP protocol.
Custom Commands: Easily extendable for additional features.
Technologies Used
Python 3.8+
Libraries:
SpeechRecognition for voice input
pyttsx3 for TTS
datetime for date and time
wikipedia for Wikipedia API
pywhatkit for additional utilities
requests for HTTP requests
dotenv for secure environment variable handling
smtplib for email
Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/AdvancedVoiceAssistant.git
cd AdvancedVoiceAssistant
2. Set Up a Virtual Environment
bash
Copy code
python -m venv venv
# Activate the environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the project root:
env
Copy code
WEATHER_API_KEY=your_openweather_api_key
EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
Replace placeholders with your API keys and credentials.
5. Run the Application
bash
Copy code
python main.py
Project Structure
plaintext
Copy code
AdvancedVoiceAssistant/
│
├── assistant.py          # Core functions for speech recognition and task handling
├── main.py               # Main logic for running the assistant
├── .env                  # Environment variables (not included in version control)
├── requirements.txt      # List of required Python libraries
├── .gitignore            # Files and directories to be ignored by Git
└── README.md             # Project documentation
Usage
Voice Commands
Time: "What’s the time?"
Date: "What’s the date today?"
Wikipedia: "Search Wikipedia for [topic]."
Weather: "What’s the weather in [city]?"
Email: "Send an email."
Provide subject and message via voice input.
Customization
Adding New Features
Open assistant.py.
Define a new function for the task.
Add a new command condition in process_command() in main.py.
Example:

python
Copy code
def greet_user():
    speak("Hello! Hope you're having a great day.")
Add to process_command():

python
Copy code
if "greet me" in command:
    greet_user()
Known Issues
Microphone Sensitivity: May need adjustment for noisy environments.
Recognition Errors: Could misinterpret speech for unclear input. Consider using additional NLP libraries for better parsing.
Future Enhancements
Integration with advanced NLP models like OpenAI's GPT for improved conversation handling.
Expandable task management (e.g., calendar scheduling).
Support for multiple languages.
