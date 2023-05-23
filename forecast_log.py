
from tkinter import *
import requests
from tkinter import messagebox 
import webbrowser

from googlesearch import search

from PIL import ImageTk, Image

import requests

class app:
    def __init__(self):
        self.main=Tk()
        self.main.geometry("800x450")
        self.main.config(bg="black")
        self.main.resizable(FALSE,FALSE)
        self.main.title("Weather Tracker")
        
        self.img = ImageTk.PhotoImage(Image.open("2527.jpg"))

        lbl_img = Label(self.main, image = self.img)
        frm_search=Frame()
        frm_search.place(x=200,y=26)
        
        self.btn_log_in=Button(self.main,text="Log-Out",font=("roboto bold",15),command=self.log)
        self.btn_log_in.place(x=700,y=5)
        
        
    
        self.en_search_bar=Entry(frm_search,width=38,font=("roboto",12))
        btn_search=Button(frm_search,text="Search",command=self.search,
                          font=("roboto",10))
        
        self.en_search_bar.grid(row=0,column=0)
        btn_search.grid(row=0,column=1)
        self.color="#ccccff"
        self.frm_weather1=Frame(self.main,width=400,height=340,background=self.color)
        

       

        self.frm_weather=Frame(self.frm_weather1,width=200,height=340,background=self.color)
        self.frm_weather.place(x=35,y=35)
        
        lbl_img.pack()

        self.frm_next_day=Frame(self.frm_weather1,background=self.color)
        self.frm_next_day.place(x=29,y=300)

        self.main.mainloop()


    def log(self):
         self.main.destroy()
         import forecast
         forecast.app()
    def search(self):
            self.frm_weather1.place(x=200,y=50)
            api_key = "545c591e52bd162a06bd7485ffb80072"
            

            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            

            city_name = self.en_search_bar.get()
            

            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            response = requests.get(complete_url)
            

            x = response.json()
            

            if x["cod"] != "404":
            
                
                y = x["main"]
                z = x["wind"]
            
            
                current_temperature = y["temp"]

                current_speed = z["speed"]
            
            
                current_pressure = y["pressure"]
            
                current_humidity = y["humidity"]
                tem=current_temperature-273.15
                
                z = x["weather"]
            
            
                self.weather_description = z[0]["description"]
    
                #Display the weather of the seacrh City
                
                lbl_city=Label(self.frm_weather,text="Location: ",font=("bold",20),background=self.color)
                lbl_city.grid(row=0,column=0)
                lbl=Label(self.frm_weather,width=15,text=city_name,font=("bold",15),background=self.color)
                lbl.grid(row=0,column=1)

            
                lbl_info=Label(self.frm_weather,text="Weather: ",font=("bold",20),background=self.color)
                lbl_info.grid(row=2,column=0)
                lbl2=Label(self.frm_weather,width=13,text=self.weather_description,font=("bold",15),background=self.color)
                lbl2.grid(row=2,column=1)

                lbl_temperature=Label(self.frm_weather,text="Temperature: ",font=("bold",20),background=self.color)
                lbl_temperature.grid(row=3,column=0)
                lbl3=Label(self.frm_weather,width=10,text=("%.2f"%tem,"°C"),font=("bold",15),background=self.color)
                lbl3.grid(row=3,column=1)

                lbl_precip=Label(self.frm_weather,text="pressure: ",font=("bold",20),background=self.color)
                lbl_precip.grid(row=4,column=0)
                lbl4=Label(self.frm_weather,width=10,text=current_pressure,font=("bold",15),background=self.color)
                lbl4.grid(row=4,column=1)

                lbl_humidity=Label(self.frm_weather,text="Humidity: ",font=("bold",20),background=self.color)
                lbl_humidity.grid(row=5,column=0)
                lbl5=Label(self.frm_weather,width=10,text=current_humidity,font=("bold",15),background=self.color)
                lbl5.grid(row=5,column=1)

                lbl_wind=Label(self.frm_weather,text="Wind: ",font=("bold",20),background=self.color)
                lbl_wind.grid(row=6,column=0)
                lbl6=Label(self.frm_weather,width=10,text=current_speed,font=("bold",15),background=self.color)
                lbl6.grid(row=6,column=1)
                
                btn_next_day=Button(self.frm_next_day,text="For More Info",width=15,font=("bold",15),command=self.next_day)
                btn_next_day.grid(row=0,column=0)

                btn_what_to_wear=Button(self.frm_next_day,text="What To Wear",width=15,font=("bold",15),command=self.cloth)
                btn_what_to_wear.grid(row=0,column=1)
                
            else:
                 messagebox.showerror(title="City",message="City Can't Find")

            

        
        
            
            
    def next_day(self):
        search1 = self.en_search_bar.get()+"weather"
        for i in search(search1, num_results=1, advanced= 1):
                webbrowser.open(i.url)
                break
        
    def cloth(self):
        w = self.weather_description

        if w == "clear sky" or w == "few clouds" or w == "scattered clouds" or w == "broken clouds" or w == "overcast clouds":
              messagebox.showinfo(title="What to wear",message="Opt for clothing made of cotton, linen, or jersey. These fabrics are breathable and help your body release heat, which can help you sweat less. So, if you want to stay cool on a hot day, stick with a cotton, linen, or jersey T-shirt.")
        
        elif w == "rain" or w == "light rain" or w == "moderate rain" or w == "heavy intensity rain" or w == "very heavy rain"or w == "extreme rain" or w == "freezing rain" or w == "light intensity shower rain" or w == "shower rain" or w == "heavy intensity shower rain" or w == "ragged shower rain":
              messagebox.showinfo(title="What to wear",message="Wear materials that are difficult to absorb water and, if they do absorb water, dry quickly. Water-resistant fabrics include synthetic fabric, silk, and wool. If they get wet, synthetic fabrics (polyester, polyamide, nylon...) are always the best option.")

        elif w == "thunderstorm" or w == "thunderstorm with light rain" or w == "thunderstorm with rain" or w == "thunderstorm with heavy rain" or w == "light thunderstorm" or w == "heavy thunderstorm" or w == "ragged thunderstorm" or w == "thunderstorm with light drizzle" or w == "thunderstorm with drizzle" or w == "thunderstorm with heavy drizzle":
              messagebox.showinfo(title="What to wear",message="Wear long sleeves, pants, and socks when you're outside. Learn how to protect yourself and your family from mosquito bites. Stay away from wild or stray animals after a storm.")
        
        elif w == "light intensity drizzle" or w == "drizzle" or w == "heavy intensity drizzle" or w == "light intensity drizzle rain" or w == "drizzle rain" or w == "" or w == "" or w == "" or w == "" or w == "":
              messagebox.showinfo(title="What to wear",smessage="Wear long sleeves, pants, and socks when you're outside. Learn how to protect yourself and your family from mosquito bites. Stay away from wild or stray animals after a storm.")

if __name__ == '__main__':
     
        app()
    
            
