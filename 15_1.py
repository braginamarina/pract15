from tkinter import *
import requests

root = Tk()

def get_weather():

    city = cityField.get()
    key = 'bdf9ea15325724f53b5773c2645d3dd2'
    url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {'appid': key, 'q': city, 'units': 'metric', 'lang': 'ru'}

    result = requests.get(url, params=params)
    weather = result.json()

    city_label.config(text=f"Город: {weather['name']}")
    temp_label.config(text=f"{weather['main']['temp']}°C")
    wind_label.config(text=f"Ветер: {weather['wind']['speed']} м/с")

root['bg'] = '#87CEFA'
root.title('Погода')
root.geometry('350x400')
root.resizable(width=False, height=False)
root.iconbitmap('cloud.ico')

frame1 = Frame(root, bg="#cefa87", width=300, height=170, bd=5, relief=RIDGE)
frame1.pack(pady = 25)
frame1.pack_propagate(False)

city_label = Label(frame1, text="город: --", font=("Arial", 14),bg="#cefa87", fg="black")
city_label.pack(pady=(15, 5))

temp_label = Label(frame1, text="--°C", font=("Arial", 40, "bold"),bg="#cefa87", fg="black")
temp_label.pack()

wind_label = Label(frame1, text="ветер: --", font=("Arial", 14),bg="#cefa87", fg="black")
wind_label.pack(pady=5)

text1 = Label(root,text="введите город:",font=("Arial", 14, 'bold'),bg="#87CEFA",fg="black")
text1.pack()

cityField = Entry(root, font=("Arial", 18, 'bold'), width=20, justify="center", bd = 5, bg = 'white', fg = 'black')
cityField.pack()

btn = Button(root,text="Поиск",font=("Arial", 16, "bold"), bg="#fa87ce", fg="white", width=15, bd = 5, command=get_weather)
btn.pack(pady = 15)

root.mainloop()