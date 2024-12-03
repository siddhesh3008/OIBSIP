import tkinter as tk
from tkinter import messagebox
from weather_api import get_weather_data
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Global unit preference
units = "metric"  # Default is Celsius

def fetch_weather():
    """
    Fetch weather data and display it on the GUI.
    """
    location = location_entry.get()
    if not location:
        messagebox.showwarning("Input Error", "Please enter a location!")
        return

    weather_data = get_weather_data(location, units)
    if not weather_data or "main" not in weather_data:
        messagebox.showerror("Error", "Failed to retrieve weather data!")
        return

    display_weather(weather_data)

def display_weather(data):
    """
    Display weather data on the GUI.
    """
    weather_frame.pack_forget()  # Clear previous weather data

    city_label.config(text=f"City: {data['name']}")
    temp_label.config(text=f"Temperature: {data['main']['temp']}°{'C' if units == 'metric' else 'F'}")
    condition_label.config(text=f"Condition: {data['weather'][0]['description'].title()}")
    wind_label.config(text=f"Wind Speed: {data['wind']['speed']} {'m/s' if units == 'metric' else 'mph'}")

    icon_code = data['weather'][0]['icon']
    update_weather_icon(icon_code)
    weather_frame.pack(pady=10)

def update_weather_icon(icon_code):
    """
    Update the weather icon using OpenWeatherMap's icon URL.
    """
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    try:
        response = requests.get(icon_url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        photo = ImageTk.PhotoImage(img)
        icon_label.config(image=photo)
        icon_label.image = photo
    except Exception as e:
        print(f"Error loading icon: {e}")

def toggle_units():
    """
    Toggle between Celsius and Fahrenheit.
    """
    global units
    units = "metric" if units == "imperial" else "imperial"
    unit_btn.config(text="Switch to °F" if units == "metric" else "Switch to °C")
    fetch_weather()

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter Location: ").pack(side=tk.LEFT)
location_entry = tk.Entry(input_frame)
location_entry.pack(side=tk.LEFT, padx=10)
tk.Button(input_frame, text="Get Weather", command=fetch_weather).pack(side=tk.LEFT)

# Weather Display Frame
weather_frame = tk.Frame(root)

city_label = tk.Label(weather_frame, font=("Helvetica", 16))
city_label.pack()

temp_label = tk.Label(weather_frame, font=("Helvetica", 14))
temp_label.pack()

condition_label = tk.Label(weather_frame, font=("Helvetica", 12))
condition_label.pack()

wind_label = tk.Label(weather_frame, font=("Helvetica", 12))
wind_label.pack()

icon_label = tk.Label(weather_frame)
icon_label.pack()

# Unit Toggle Button
unit_btn = tk.Button(root, text="Switch to °F", command=toggle_units)
unit_btn.pack(pady=10)

root.mainloop()
