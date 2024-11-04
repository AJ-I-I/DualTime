import tkinter as tk                # IMPORTS
from datetime import datetime       # tkinter, datetime, pytz, requests
import pytz                         # use format pip install (import name here) to ensure program runs
import requests

# Constants
API_KEY = '#Insert your openweathermap API key here'
CITY_1 = 'Boston'
CITY_2 = 'Los Angeles'
TIMEZONE_1 = 'America/New_york'
TIMEZONE_2 = 'America/Los_Angeles'

# Function to get current time and weather
def get_time_and_weather():
    try:
        # Get current time for each timezone
        now_1 = datetime.now(pytz.timezone(TIMEZONE_1)).strftime('%I:%M:%S:%p')
        now_2 = datetime.now(pytz.timezone(TIMEZONE_2)).strftime('%I:%M:%S:%p')

        # Fetch weather information
        weather_1 = get_weather(CITY_1)
        weather_2 = get_weather(CITY_2)

        # Update labels
        time_label_1.config(text=f"{CITY_1} Time: {now_1}")
        weather_label_1.config(text=f"{CITY_1} Weather: {weather_1}")
        time_label_2.config(text=f"{CITY_2} Time: {now_2}")
        weather_label_2.config(text=f"{CITY_2} Weather: {weather_2}")

        # Refresh every minute
        root.after(60000, get_time_and_weather)
    except Exception as e:
        print(f"Error: {e}")

# Function to get weather from OpenWeatherMap
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        return f"{temp}°C, {description.capitalize()}"
    else:
        return "Weather data unavailable"

# GUI setup
root = tk.Tk()
root.title("Dual Time Zone Display")
root.geometry("400x200")
root.configure(background='black')

# Labels for City 1
time_label_1 = tk.Label(root, font=('courier', 12), fg='#00cc36', bg='#000')
time_label_1.pack(pady=5)
weather_label_1 = tk.Label(root, font=('courier', 10), fg='#00cc36', bg='#000')
weather_label_1.pack(pady=5)

# Labels for City 2
time_label_2 = tk.Label(root, font=('courier', 12), fg='#00cc36', bg='#000')
time_label_2.pack(pady=5)
weather_label_2 = tk.Label(root, font=('courier', 10), fg='#00cc36', bg='#000')
weather_label_2.pack(pady=5)

# Start fetching data
get_time_and_weather()

# Start the GUI loop
root.mainloop()
