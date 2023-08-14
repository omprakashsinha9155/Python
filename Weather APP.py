'''
import tkinter as tk
from PIL import Image,ImageTk     # pip install pillow

root = tk.Tk()


root.title("Weather APP")
root.geometry("600x500")

img = Image.open('./op.png')
img = img.resize((600,500),Image.ANTIALIAS)
img_photo = ImageTk.photoImage()Image(img)


bg_lbl = tk.Label(root,image = img_photo)
bg_lbl.place(x=0, y=0, width=600, height=500)

root.mainloop()
'''

import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    own_data = requests.get(api).json()
    condition = own_data['weather'][0]['main']
    temp = int(own_data['main']['temp'] - 273.15)
    min_temp = int(own_data['main']['temp_min'] - 273.15)
    max_temp = int(own_data['main']['temp_max'] - 273.15)
    pressure = own_data['main']['pressure']
    humidity = own_data['main']['humidity']
    wind = own_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(own_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(own_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()