import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def get_weather():
    # Location
    city = text.get()
    geolocator = Nominatim(user_agent="geopyExercises")
    location = geolocator.geocode(city)
    lat = location.latitude
    long = location.longitude
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=long, lat=lat)
    city_lbl.config(text=city)
    
    # Time
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock_lbl.config(text=current_time)
    time_lbl.config(text="Local Time")
    
    # Weather
    api_key = '4b28f169f63a5d76d0ee43f10c933fe4'
    api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}'
    jsondata = requests.get(api).json()
    condition = jsondata["weather"][0]["main"]
    description = jsondata["weather"][0]["description"]
    temp = int(jsondata["main"]['temp'] - 273.15)
    pressure = jsondata["main"]["pressure"]
    humidity = jsondata["main"]["humidity"]
    wind_speed = jsondata["wind"]["speed"]
    temp_lbl.config(text=f'{temp} °C')
    wind_lbl.config(text=f'{wind_speed} m/s')
    humidity_lbl.config(text=f'{humidity} %')
    descreption_lbl.config(text=description)
    pressure_lbl.config(text=f'{pressure} hPa')

window = tk.Tk()
window.title("Weather App")
window.geometry("900x500+300+200")
window.resizable(False,False)

# Search bar
search_image = tk.PhotoImage(file="search.png")
search_image_label = tk.Label(window, image=search_image)
search_image_label.pack(side=tk.TOP, pady=10)

text = tk.Entry(window, justify="center", width=17, font=('Verdana', 25, 'bold'), bg="#404040", fg="white", border=0)
text.place(x=250, y=25)

Magnifyingglass = tk.PhotoImage(file="search_icon.png")
Magnifyingglass_Btn = tk.Button(window, image=Magnifyingglass, border=0, cursor='hand2', bg="#404040", command=get_weather)
Magnifyingglass_Btn.place(x=590, y=22)

# Logo
logo = tk.PhotoImage(file="4052984.png")
logo_lbl = tk.Label(window, image=logo)
logo_lbl.pack(side=tk.TOP)

frame_image = tk.PhotoImage(file="box.png")
frame_image_label = tk.Label(window, image=frame_image)
frame_image_label.pack(side=tk.BOTTOM, pady=10)

# City Name
city_lbl = tk.Label(window, font=("Verdana", 40, "bold"), fg="#cbe355")
city_lbl.place(x=120, y=160)

# Time
time_lbl = tk.Label(window, font=("Verdana", 20, "bold"), fg="#4b4bcc")
time_lbl.place(x=120, y=230)

# Clock
clock_lbl = tk.Label(window, font=("Helvetica", 20), fg="#4b4bcc")
clock_lbl.place(x=120, y=270)

# Labels
Label1 = tk.Label(window, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
Label1.place(x=120, y=400)

Label2 = tk.Label(window, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
Label2.place(x=280, y=400)

Label3 = tk.Label(window, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
Label3.place(x=450, y=400)

Label4 = tk.Label(window, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
Label4.place(x=670, y=400)

wind_lbl = tk.Label(window, text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="#404040")
wind_lbl.place(x=120, y=430)

humidity_lbl = tk.Label(window, text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="#404040")
humidity_lbl.place(x=280, y=430)

descreption_lbl = tk.Label(window, text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="#404040")
descreption_lbl.place(x=450, y=430)

pressure_lbl = tk.Label(window, text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="#404040")
pressure_lbl.place(x=670, y=430)

temp_lbl = tk.Label(window, text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="#404040")
temp_lbl.place(x=120, y=470)

window.mainloop()
