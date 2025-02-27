import tkinter as tk
from tkinter import ttk
import requests
import json
import io
from datetime import datetime

def get_weather():
    """Fetch weather data for the given city"""
    CityName=city_entry.get()
    #APIkey
    api_key="0fb23a4284825b978c837143965f49a0"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={CityName}&appid={api_key}"
    reponse=requests.get(url)
    data=reponse.json()
    temp=data["main"]["temp"]
    temp_value.config(text=f"{temp}")
    humidity_value.config(text=f"Humidity:{data["main"]["humidity"]}")
    wind_value.config(text=f"Wind Speed:{data["wind"]["speed"]}")  
    city_value.config(text=f"City:{data["name"]}")

    weather_data = {
        "city": data["name"],
        "temperature":data["main"]["temp"],
        "condition": data["weather"][0]["main"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "time": datetime.now().strftime("%H:%M - %d %b %Y")
    }
    display_weather(weather_data)

def display_weather(data):
    """Update UI with weather data"""
    city_value.config(text=data["city"])
    temp_value.config(text=data["temperature"])
    condition_value.config(text=data["condition"])
    humidity_value.config(text=data["humidity"])
    wind_value.config(text=data["wind"])
    time_value.config(text=data["time"])
    
    # Update weather icon based on condition (simplified example)
    condition = data["condition"].lower()
    if "clouds" in condition:
        weather_icon.config(text="☁️")
    elif "clear" in condition :
        weather_icon.config(text="☀️")
    elif "rain" in condition:
        weather_icon.config(text="🌧️")
    elif "snow" in condition:
        weather_icon.config(text="❄️")
    else:
        weather_icon.config(text="🌤️")

# Global variables
search_history = []


# Initialize main window
window = tk.Tk()
window.title("Weather App")
window.geometry("900x600")
window.configure(bg="#f5f5f5")

# Apply custom style
style = ttk.Style()
style.configure("TButton", font=("Roboto", 12), background="#4CAF50")
style.configure("TEntry", font=("Roboto", 12))
style.configure("TFrame", background="#f5f5f5")

# Create main containers
header_frame = tk.Frame(window, bg="#2196F3", padx=20, pady=15)
header_frame.pack(fill="x")

content_container = tk.Frame(window, bg="#f5f5f5")
content_container.pack(fill="both", expand=True, padx=20, pady=20)

# Left panel for search and history
left_panel = tk.Frame(content_container, bg="white", padx=20, pady=20, bd=1, relief="solid")
left_panel.pack(side="left", fill="y", padx=(0, 10))

# Right panel for weather display
right_panel = tk.Frame(content_container, bg="white", padx=30, pady=30, bd=1, relief="solid")
right_panel.pack(side="right", fill="both", expand=True)

# Header content
title_label = tk.Label(
    header_frame,
    text="Weatheria",
    font=("Roboto", 30, "bold"),
    bg="#2196F3",
    fg="white"
)
title_label.pack(side="left")

# Search section in left panel
search_label = tk.Label(
    left_panel,
    text="Search Location",
    font=("Roboto", 14, "bold"),
    bg="white",
    fg="#333333"
)
search_label.pack(anchor="w", pady=(0, 10))

search_frame = tk.Frame(left_panel, bg="white")
search_frame.pack(fill="x", pady=(0, 20))

city_entry = ttk.Entry(
    search_frame,
    font=("Roboto", 12),
    width=18
)
city_entry.pack(side="left", fill="x", expand=True)


search_button = tk.Button(
    search_frame,
    text="Search",
    font=("Roboto", 11),
    bg="#2196F3",
    fg="white",
    activebackground="#1976D2",
    cursor="hand2",
    padx=10,
    command=get_weather
)
search_button.pack(side="left", padx=(10, 0))

# Weather display in right panel
weather_display_frame = tk.Frame(right_panel, bg="white")
weather_display_frame.pack(fill="both", expand=True)

# City and time info
info_frame = tk.Frame(weather_display_frame, bg="white")
info_frame.pack(fill="x", pady=(0, 20))

city_value = tk.Label(
    info_frame,
    text="City Name",
    font=("Roboto", 24, "bold"),
    bg="white",
    fg="#333333"
)
city_value.pack(side="left")

time_value = tk.Label(
    info_frame,
    text="Time - Date",
    font=("Roboto", 12),
    bg="white",
    fg="#757575"
)
time_value.pack(side="right", pady=10)

# Main weather info
main_weather_frame = tk.Frame(weather_display_frame, bg="white")
main_weather_frame.pack(fill="x", pady=10)

weather_icon = tk.Label(
    main_weather_frame,
    text="🌤️",
    font=("Segoe UI Emoji", 72),
    bg="white",
    fg="#FF9800"
)
weather_icon.pack(side="left", padx=(0, 20))

temp_frame = tk.Frame(main_weather_frame, bg="white")
temp_frame.pack(side="left")

temp_value = tk.Label(
    temp_frame,
    text="--°C",
    font=("Roboto", 42, "bold"),
    bg="white",
    fg="#333333"
)
temp_value.pack(anchor="w")

condition_value = tk.Label(
    temp_frame,
    text="Weather Condition",
    font=("Roboto", 16),
    bg="white",
    fg="#757575"
)
condition_value.pack(anchor="w")

# Divider
divider = ttk.Separator(weather_display_frame, orient="horizontal")
divider.pack(fill="x", pady=30)

# Additional weather details
details_frame = tk.Frame(weather_display_frame, bg="white")
details_frame.pack(fill="x")

# Humidity
humidity_frame = tk.Frame(details_frame, bg="white")
humidity_frame.pack(side="left", expand=True, fill="x")

humidity_label = tk.Label(
    humidity_frame,
    text="HUMIDITY",
    font=("Roboto", 12),
    bg="white",
    fg="#757575"
)
humidity_label.pack(anchor="w")

humidity_value = tk.Label(
    humidity_frame,
    text="--%",
    font=("Roboto", 20, "bold"),
    bg="white",
    fg="#333333"
)
humidity_value.pack(anchor="w", pady=(5, 0))

# Wind
wind_frame = tk.Frame(details_frame, bg="white")
wind_frame.pack(side="left", expand=True, fill="x")

wind_label = tk.Label(
    wind_frame,
    text="WIND SPEED",
    font=("Roboto", 12),
    bg="white",
    fg="#757575"
)
wind_label.pack(anchor="w")

wind_value = tk.Label(
    wind_frame,
    text="-- km/h",
    font=("Roboto", 20, "bold"),
    bg="white",
    fg="#333333"
)
wind_value.pack(anchor="w", pady=(5, 0))

# Footer
footer_frame = tk.Frame(window, bg="#E0E0E0", padx=10, pady=5)
footer_frame.pack(fill="x", side="bottom")

footer_label = tk.Label(
    footer_frame,
    text="© 2025 Weather Dashboard • Powered by Modern Weather API",
    font=("Roboto", 10),
    bg="#E0E0E0",
    fg="#757575"
)
footer_label.pack(side="right")

# Run the main loop
window.mainloop()