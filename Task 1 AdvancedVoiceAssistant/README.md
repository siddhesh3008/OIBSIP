# Advanced Voice Assistant in Python

A Python-based voice assistant designed to perform various tasks such as fetching the current time and date, retrieving weather updates, searching Wikipedia, and sending emails. This project demonstrates the integration of Speech Recognition, Natural Language Processing (NLP), and API-based task automation, offering a foundation for building custom, voice-controlled applications.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Introduction

The Advanced Voice Assistant is a versatile tool that leverages Python's capabilities for speech recognition and task automation. It can perform a wide range of tasks and is highly extendable, making it suitable for educational purposes, personal use, or as a starting point for more complex AI-driven assistants.

## Features

- **Speech Recognition**: Converts spoken words into text using the `SpeechRecognition` library.
- **Text-to-Speech (TTS)**: Provides audio feedback using `pyttsx3`.
- **Wikipedia Search**: Retrieves concise summaries from Wikipedia.
- **Weather Updates**: Fetches real-time weather data using the OpenWeather API.
- **Email Functionality**: Sends emails through Gmail with the SMTP protocol.
- **Custom Commands**: Easily extendable for additional functionality.

## Technologies Used

### Language:
- Python 3.8+

### Libraries:
- **[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)**: For capturing and processing voice input.
- **[pyttsx3](https://pypi.org/project/pyttsx3/)**: For text-to-speech conversion.
- **datetime**: Built-in library for handling date and time.
- **[wikipedia](https://pypi.org/project/wikipedia/)**: For accessing the Wikipedia API.
- **[pywhatkit](https://pypi.org/project/pywhatkit/)**: For additional utilities.
- **[requests](https://pypi.org/project/requests/)**: For making HTTP requests (used for weather data).
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: For secure environment variable handling.
- **smtplib**: Built-in library for email functionality.
