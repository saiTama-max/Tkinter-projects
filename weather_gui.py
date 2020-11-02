from tkinter import *
import requests
import json


# my_key = NOKEY
root = Tk()
root.title("weather")
root.geometry('250x250')




# img_cloud = ImageTk.PhotoImage(Image.open('images/cloud_img_re.jpg'))


def search():
    # global weather
    # global country
    # global place
    # global lbl1
    # global lbl2
    # global temp
    try:
        api_request = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=' + zipcode_ent.get() + ',' + country_ent.get() + f'&appid=a715a0439b4c43699f72a0b1d291295b')
        api = json.loads(api_request.content)
        # print(api)

        if api['weather'][0]['main'] == 'Clouds':
            weather_color = '#B0A99F'
            country_color = '#B0A99F'
            place_color = '#B0A99F'
            temp_color = '#B0A99F'
            lbl_color = '#B0A99F'
            # lbl_bg.config(image=img_cloud)
            

        elif api['weather'][0]['main'] == 'Rain':
            place_color = '#afc3cc'
            weather_color = '#afc3cc'
            country_color = '#afc3cc'
            temp_color = '#afc3cc'
            lbl_color = '#afc3cc'

        elif api['weather'][0]['main'] == 'Mist':
            place_color = '#f0ffff'
            weather_color = '#f0ffff'
            country_color = '#f0ffff'
            temp_color = '#f0ffff'
            lbl_color = '#f0ffff'

        elif api['weather'][0]['main'] == 'Clear':
            place_color = '#FFFF99'
            weather_color = '#FFFF99'
            country_color = '#FFFF99'
            temp_color = '#FFFF99'
            lbl_color = '#FFFF99'

        else:
            place_color = 'light grey'
            weather_color = 'light grey'
            country_color = 'light grey'
            temp_color = 'light grey'
            lbl_color = 'light grey'


        

        weather_data = (api['weather'][0]['main'])
        weather.config(text=f'Weather:   {weather_data}', bg=weather_color)

        country_data = api['sys']['country']
        country.config(text=f"Country:    {country_data}", bg=country_color)

        place_data = api['name']
        place.config(text=f"Place:   {place_data}", bg=place_color)

        temp_data = api['main']['temp']
        temp.config(text=f'Temperature: {int(temp_data - 273.15)}°C', bg=temp_color)

        lbl1.config(bg=lbl_color, anchor=W)
        lbl2.config(bg=lbl_color, anchor=W)
        root.config(bg=lbl_color)

    except Exception as e:
        api = 'Error..'
        print("error")


img = PhotoImage(file='images/magnifying-glass.png')
zipcode_ent = Entry(root)
zipcode_ent.place(x=50, y=10)

search_btn = Button(root, image=img, command=search, cursor='dot', activebackground='light grey')
search_btn.place(height=50, x=220, y=10)

country_ent = Entry(root)
country_ent.place(x=50, y=40)

weather = Label(root, borderwidth=0, highlightthickness=0)
weather.place(x=70, y=70)

country = Label(root, borderwidth=0, highlightthickness=0)
country.place(x=70, y=100)

place = Label(root, borderwidth=0, highlightthickness=0)
place.place(x=70, y=130)

temp = Label(root, borderwidth=0, highlightthickness=0)
temp.place(x=70, y=160)

lbl1 = Label(root, text='zipcode')
lbl1.place(x=0, y=10)
lbl2 = Label(root, text='country')
lbl2.place(x=0, y=40)

# afc3cc
# B0A99F
# f0ffff
# FFFF99
#5ca68d

root.mainloop()