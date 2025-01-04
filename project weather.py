#importing modules
import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

# Function to get notification of weather report
def getNotification():
    cityName = place.get()  # getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  # base URL from where we extract weather report
    
    try:
        # This is the complete URL to get weather conditions of a city
        complete_url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
        response = requests.get(complete_url)  # requesting for the content of the URL
        x = response.json()  # converting it into JSON
        
        # checking if the city is found in the API response
        if x["cod"] != "404":
            y = x["main"]  # getting the "main" key from the JSON object

            # getting the "temp" key of y
            temp = y["temp"]
            temp -= 273  # converting temperature from Kelvin to Celsius

            # storing the value of the "pressure" key of y
            pres = y["pressure"]

            # getting the value of the "humidity" key of y
            hum = y["humidity"]

            # storing the value of "weather" key in variable z
            z = x["weather"]

            # getting the corresponding "description"
            weather_desc = z[0]["description"]

            # combining the above values as a string 
            info = (f"Here is the weather description of {cityName}:\n"
                    f"Temperature = {temp}°C\n"
                    f"Atmospheric Pressure = {pres} hPa\n"
                    f"Humidity = {hum}%\n"
                    f"Description of the Weather = {weather_desc}")

            # showing the notification 
            notification.notify(
                title="WEATHER REPORT",
                message=info,
                timeout=2  # displaying time
            )
            
            # waiting time
            time.sleep(7)
        else:
            mb.showerror("Error", "City Not Found! Please enter a valid city name.")
    
    except Exception as e:
        mb.showerror('Error', str(e))  # show pop-up message if any error occurred
        
# creating the window
wn = Tk()
wn.title("Weather Notifier")
wn.geometry('700x200')
wn.config(bg='azure')

# Heading label
Label(wn, text="Weather Notifier", font=('Courier', 15), fg='grey19', bg='azure').place(x=100, y=15)

# Getting the place name 
Label(wn, text='Enter the Location:', font=("Courier", 13), bg='azure').place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

# Button to get notification
btn = Button(wn, text='Get Notification', font=7, fg='grey19', command=getNotification)
btn.place(relx=0.4, rely=0.75)

# run the window till closed by user
wn.mainloop()
