import tkinter as tk
import requests
from tkinter import messagebox

API_KEY = "a11953c25ff86d5badc59a865f00e31f"

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = { "q": city,"appid": API_KEY,"units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def show_weather():
    city = city_entry.get()
    if city:
        weather_data = get_weather(city)
        if weather_data["cod"] == 200:
            temperature = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            messagebox.showinfo("Weather", f"Temperature: {temperature}°C\nDescription: {description}")
        else:
            messagebox.showerror("Error", "City not found.")
    else:
        messagebox.showerror("Error", "Please enter a city.")

priya = tk.Tk()
priya.title("Weather Application")
priya.geometry("250x250")

city_label = tk.Label(priya, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(priya)
city_entry.pack()

get_weather_button = tk.Button(priya, text="search Weather", command=show_weather)
get_weather_button.pack()

made_1 = tk.Label(priya,text="Made by: Padmapriya")
made_1.pack()

priya.mainloop()
