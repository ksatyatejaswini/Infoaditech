from tkinter import *
import requests
import json
from datetime import datetime, timedelta 

def get_weather():
    city = city_entry.get()
    api_key = "e803c5601d2a032f59688f8c87bab90b"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = json.loads(response.text)

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather_condition = data["weather"][0]["description"]
        result_label.config(
            text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nWeather Condition: {weather_condition}"
        )
    else:
        result_label.config(text="City not found")

def save_favorite():
    city = city_entry.get()
    favorites_listbox.insert(END, city)

def view_forecast():
    selected_city = favorites_listbox.get(ANCHOR)
    if selected_city:
        api_key = "e803c5601d2a032f59688f8c87bab90b"
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={selected_city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = json.loads(response.text)
        if data["cod"] == "200":
            forecast = data["list"]
            forecast_text = "Next Five Days Forecast:\n"
            today = datetime.now()
            for item in forecast:
                timestamp = item['dt']
                dt_object = datetime.utcfromtimestamp(timestamp)
                if dt_object > today:
                    date = dt_object.strftime('%d-%m-%Y')
                    temperature = item['main']['temp']
                    forecast_text += f"{date} {temperature}°C\n"
                    today += timedelta(days=1)
            forecast_label.config(text=forecast_text)
        else:
            forecast_label.config(text="Forecast not available for this city")

root = Tk()
root.title("Weather App")
root.geometry("400x600")
root.configure(bg="skyblue")

city_label = Label(root, text="Enter City:" ,bg="skyblue" , font="20")
city_label.pack()

city_entry = Entry(root)
city_entry.pack()

search_button = Button(root, text="Search", command=get_weather, bg="yellow")
search_button.pack()

result_label = Label(root, text="", bg="skyblue" ,font="20")
result_label.pack()

favorites_label = Label(root, text="Favorites:" ,bg="skyblue",font="20")
favorites_label.pack()

favorites_listbox = Listbox(root)
favorites_listbox.pack()

save_button = Button(root, text="Save Favorite", command=save_favorite , bg="yellow")
save_button.pack()

forecast_button = Button(root, text="View Forecast", command=view_forecast, bg="yellow")
forecast_button.pack()

forecast_label = Label(root, text="", bg="skyblue",font="20")
forecast_label.pack()

root.mainloop()
