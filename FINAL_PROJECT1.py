"""
    FINAL PROJECT PRO-101 
    GROUP MEMBERS: Khiev Oudom
                   Chhay Porheng
                   Prim Nichhay
                   Chhayrong Daravid
    PROJECT: Horoscope
"""


from tkinter import *
from tkinter.font import BOLD
import pyaztro
from tkcalendar import *
from tkcalendar import DateEntry
import pandas as pd 
import mysql.connector

con = mysql.connector.connect(host='localhost', user='daravid', password='12311474', database='final_project')
mycursor = con.cursor()
zodiac = mycursor.execute("CREATE TABLE IF NOT EXISTS zodiac (id INT(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), DOB VARCHAR(255), sign VARCHAR(255))")
kh_horo = mycursor.execute("CREATE TABLE IF NOT EXISTS kh (id INT(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), DOB VARCHAR(255), sign VARCHAR(255))")

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

def windows_size(title,width,height):
    xyz.title(str(title))
    win_width = xyz.winfo_screenwidth()
    win_height = xyz.winfo_screenheight()
    x = int((win_width - width)/2)
    y = int((win_height- height)/2)
    xyz.resizable(True,True)
    xyz.minsize(int(width-(width*0.2)), int(height-(height*0.2)))
    xyz.maxsize(int(win_width), int(win_height))
    xyz.geometry('%dx%d+%d+%d'%(width,height,x,y))

#=====================================Result=========================================================================================
def HOROSCOPE():
    def windows_size(title,width,height):
        H.title(str(title))
        win_width = H.winfo_screenwidth()
        win_height = H.winfo_screenheight()
        x = int((win_width - width)/2)
        y = int((win_height- height)/2)
        H.resizable(True,True)
        H.minsize(int(width-(width*0.2)), int(height-(height*0.2)))
        H.maxsize(int(win_width), int(win_height))
        H.geometry('%dx%d+%d+%d'%(width,height,x,y))

    dic_horos = {
            "month":(12, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11),
            "day":(22,20,19,21,20,21,21,23,23,23,23,22),
            "astro_sign": ("Sagittarius", "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio"),
            "result": (0,1,2,3,4,5,6,7,8,9,10,11),
            "kh_sign": ("Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Mouse", "Cow", "Tiger", "Rabbit"), 
            "kh_num": ("1, 6, 7", "2, 8, 9", "2, 3, 7", "2, 7", "4, 9", "5, 7, 8", "3, 4, 9", "2, 5, 8", "2, 3", "1, 4", "1, 3, 4", "3, 4, 6"),
            "kh_color": ("Gold & Silver", "Black, Red, Yellow", "Yellow, Green", "Brown, Red, Purple", "White, Blue, Gold", "Gold, Brown, Yellow", "Red, Green, Purple", "Yellow, Gray, Brown, Gold", "Blue, Gold, Green", "White, Yellow, Green", "Blue, Gray, Orange", "Red, Pink, Purple, Blue"),
            "kh_flower": ("Dragon flower", "Orchid, Cactus", "Calla Lily, Jasmine", "Carnations, Primroses", "Chrysanthemum, Crape myrtle", "Gladiola, Cockscomb", "Rose, Cymbidium orchids", "Hydrangea and Daisy", "Lily, African violet", "Tulip, Peach blossom", "Yellow lily, Cineraria", "Plantain lily, Jasmine"),
            "kh_direction": ("east, north, south", "east, west, and southwest", "east, west, and south", "north", "north, northwest, west", "south, southeast", "east, south, and northeast", "east and southwest", "west, northwest and southwest", "north, south", "east, north, south", "east, south and northwest")
        }

    class DOB:
        def __init__(self, year, month, day):
            self.year = year
            self.day = day
            self.month = month
    class Horoscope(DOB):
        def Eu_Horoscope(self):
            mycanva1.create_text(240, 80, text="EU_Horoscope", font=('Microsoft Yahei UI', 30, BOLD), fill='white')
            mycanva1.create_text(935, 80, text="KH_Horoscope", font=('Microsoft Yahei UI', 30, BOLD), fill='white')
            mycanva1.create_line(600, 0, 600, 630, fill='white')
            # running in for loop to auto compare and martch the astro_sign with month & day
            for i in range(len(dic_horos["month"])):
                if self.month == dic_horos["month"][i]:
                    if self.day < dic_horos["day"][i]:
                        self.astro_signs = dic_horos["astro_sign"][i]
                    else:
                        if self.month == 11:
                            self.astro_signs = dic_horos["astro_sign"][0]
                        else:
                            self.astro_signs = dic_horos["astro_sign"][i+1]
            des = pyaztro.Aztro(sign = self.astro_signs)

            mycanva1.create_text(230, 150, text=self.astro_signs, font=('Microsoft Yahei UI', 25, BOLD), fill='white')
            mycanva1.create_text(225, 220, text="Mood:    "+str(des.mood), font=('Microsoft Yahei UI', 12, BOLD), fill='white')
            mycanva1.create_text(225, 250, text="Lucky Number:    "+str(des.lucky_number), font=('Microsoft Yahei UI', 12, BOLD), fill='white')
            mycanva1.create_text(225, 280, text="Lucky Time:    "+str(des.lucky_time), font=('Microsoft Yahei UI', 12, BOLD), fill='white')
            mycanva1.create_text(225, 310, text="Lucky Color:    "+str(des.color), font=('Microsoft Yahei UI', 12, BOLD), fill='white')
            mycanva1.create_text(225, 340, text="Lucky Compatibility:    "+str(des.compatibility), font=('Microsoft Yahei UI', 12, BOLD), fill='white')
            
            
            val = "INSERT INTO zodiac (name, DOB, sign) VALUES (%s, %s, %s)"
            sql = (str(entry1.get()), str(cal.get()), str(self.astro_signs))
            mycursor.execute(val, sql)
            con.commit()
            
            if str(self.astro_signs) == "Aquarius":
                return mycanva1.create_image(120,400,image=immg1, anchor='nw')
            elif str(self.astro_signs) == "Aries":
                return mycanva1.create_image(120,400,image=immg2, anchor='nw')
            elif str(self.astro_signs) == "Cancer":
                return mycanva1.create_image(120,400,image=immg3, anchor='nw')
            elif str(self.astro_signs) == "Capricorn":
                return mycanva1.create_image(120,400,image=immg4, anchor='nw')
            elif str(self.astro_signs) == "Gemini":
                return mycanva1.create_image(120,400,image=immg5, anchor='nw')
            elif str(self.astro_signs) == "Leo":
                return mycanva1.create_image(120,400,image=immg6, anchor='nw')
            elif str(self.astro_signs) == "Libra":
                return mycanva1.create_image(120,400,image=immg7, anchor='nw')
            elif str(self.astro_signs) == "Pisces":
                return mycanva1.create_image(120,400,image=immg8, anchor='nw')
            elif str(self.astro_signs) == "Sagittarius":
                return mycanva1.create_image(120,400,image=immg9, anchor='nw')
            elif str(self.astro_signs) == "Scorpio":
                return mycanva1.create_image(120,400,image=immg10, anchor='nw')
            elif str(self.astro_signs) == "Taurus":
                return mycanva1.create_image(120,400,image=immg11, anchor='nw')
            elif str(self.astro_signs) == "Virgo":
                return mycanva1.create_image(120,400,image=immg12, anchor='nw')             

        def Kh_Horoscope(self):
            x = abs(self.year - 2000) % 12
            for i in range(len(dic_horos["result"])):
                if x == dic_horos["result"][i]:
                    if self.month > dic_horos["month"][3]:
                        self.kh_sign = dic_horos["kh_sign"][i]
                        self.kh_num = dic_horos["kh_num"][i]
                        self.kh_color = dic_horos["kh_color"][i]
                        self.kh_flower = dic_horos["kh_flower"][i]
                        self.kh_direction = dic_horos["kh_direction"][i]            
                    else:
                        if self.month == 12:
                            self.kh_sign = dic_horos["kh_sign"][i]
                            self.kh_num = dic_horos["kh_num"][i]
                            self.kh_color = dic_horos["kh_color"][i]
                            self.kh_flower = dic_horos["kh_flower"][i]
                            self.kh_direction = dic_horos["kh_direction"][i]
                        else:
                            self.kh_sign = dic_horos["kh_sign"][i - 1]
                            self.kh_num = dic_horos["kh_num"][i - 1]
                            self.kh_color = dic_horos["kh_color"][i - 1]
                            self.kh_flower = dic_horos["kh_flower"][i - 1]
                            self.kh_direction = dic_horos["kh_direction"][i - 1]
                            
            mycanva1.create_text(900, 150, text=self.kh_sign, font=('Microsoft Yahei UI', 25, BOLD), fill='white')
            mycanva1.create_text(880, 230, text="Lucky Number:    "+str(self.kh_num), font=('Microsoft Yahei UI', 12, BOLD), fill='white')
            mycanva1.create_text(880, 260, text="Lucky Color:    "+str(self.kh_color), font=('Microsoft Yahei UI', 12, BOLD), fill='white')
            mycanva1.create_text(880, 290, text="Lucky Flower:    "+str(self.kh_flower), font=('Microsoft Yahei UI', 12, BOLD), fill='white')
            mycanva1.create_text(920, 320, text="Lucky Direction:    "+str(self.kh_direction), font=('Microsoft Yahei UI', 12, BOLD), fill='white')
          
            val1 = "INSERT INTO kh (name, DOB, sign) VALUES (%s, %s, %s)"
            sql1 = (str(entry1.get()), str(cal.get()), str(self.kh_sign))
            mycursor.execute(val1, sql1)
            con.commit()

            if str(self.kh_sign) == "Dragon":
                return mycanva1.create_image(800,340,image=Img1, anchor='nw')
            elif str(self.kh_sign) == "Snake":
                return mycanva1.create_image(800,340,image=Img2, anchor='nw')
            elif str(self.kh_sign) == "Horse":
                return mycanva1.create_image(800,340,image=Img3, anchor='nw')
            elif str(self.kh_sign) == "Goat":
                return mycanva1.create_image(800,340,image=Img4, anchor='nw')
            elif str(self.kh_sign) == "Monkey":
                return mycanva1.create_image(800,340,image=Img5, anchor='nw')
            elif str(self.kh_sign) == "Rooster":
                return mycanva1.create_image(800,340,image=Img6, anchor='nw')
            elif str(self.kh_sign) == "Dog":
                return mycanva1.create_image(800,340,image=Img7, anchor='nw')
            elif str(self.kh_sign) == "Pig":
                return mycanva1.create_image(800,340,image=Img8, anchor='nw')
            elif str(self.kh_sign) == "Mouse":
                return mycanva1.create_image(800,340,image=Img9, anchor='nw')
            elif str(self.kh_sign) == "Cow":
                return mycanva1.create_image(800,340,image=Img10, anchor='nw')
            elif str(self.kh_sign) == "Tiger":
                return mycanva1.create_image(800,340,image=Img11, anchor='nw')
            elif str(self.kh_sign) == "Rabbit":
                return mycanva1.create_image(800,340,image=Img12, anchor='nw')

    H = Toplevel(xyz)
    windows_size("Horoscope", 1200, 630)
    H.resizable(False, False)

    imgs = PhotoImage(file='Image/horoscope2.png')
    Img1 = PhotoImage(file="Image/Dragons.png")
    Img2 = PhotoImage(file="Image/Snakes.png")
    Img3 = PhotoImage(file="Image/Horses.png")
    Img4 = PhotoImage(file="Image/Goats.png")
    Img5 = PhotoImage(file="Image/Monkeys.png")
    Img6 = PhotoImage(file="Image/Roosters.png")
    Img7 = PhotoImage(file="Image/Dogs.png")
    Img8 = PhotoImage(file="Image/Pigs.png")
    Img9 = PhotoImage(file="Image/Mouses.png")
    Img10 = PhotoImage(file="Image/Cows.png")
    Img11 = PhotoImage(file="Image/Tigers.png")
    Img12 = PhotoImage(file="Image/Rabbits.png")

    immg1 = PhotoImage(file="Image/Aquariuss.png")
    immg2 = PhotoImage(file="Image/Ariess.png")
    immg3 = PhotoImage(file="Image/Cancers.png")
    immg4 = PhotoImage(file="Image/Capricorns.png")
    immg5 = PhotoImage(file="Image/Geminis.png")
    immg6 = PhotoImage(file="Image/Leos.png")
    immg7 = PhotoImage(file="Image/Libras.png")
    immg8 = PhotoImage(file="Image/piscess.png")
    immg9 = PhotoImage(file="Image/Saggitarius-removebg-preview.png")
    immg10 = PhotoImage(file="Image/Scorpios.png")
    immg11 = PhotoImage(file="Image/Tauruss.png")
    immg12 = PhotoImage(file="Image/Virgos.png")
    
    mycanva1 = Canvas(H, width=1200, height=630)
    mycanva1.pack(fill='both', expand=True)
    mycanva1.create_image(0,0,image=imgs, anchor='nw')

    Hoo = str(cal.get_date())
    dayyy = pd.to_datetime(Hoo).day
    M = pd.to_datetime(Hoo).month
    Y = pd.to_datetime(Hoo).year
    myhoros = Horoscope(Y, M, dayyy)
    myhoros.Eu_Horoscope()
    myhoros.Kh_Horoscope()
    
    H.mainloop()

#======================================================RESULT=====================================================================




xyz = Tk()
windows_size("Horoscope", 400, 300)
xyz.resizable(False, False)
Img = PhotoImage(file='Image/hoho.png')

#=======================Create Canvas================================
mycanva = Canvas(xyz, width=400, height=300)
mycanva.pack(fill='both', expand=True)
#==========================Applying background image==========================
mycanva.create_image(0,0,image=Img, anchor='nw')
#==========================Add the title HOROSCOPE
mycanva.create_text(200, 50, text='HOROSCOPE', font=('Microsoft Yahei UI', 25, BOLD), fill='white')

#=================Combo Box======================================
entry1 = Entry(mycanva, width=20, fg='black', font=('Microsoft Yahei UI Light', 8, BOLD))
entry1.place(x=130, y=100)
mycanva.create_text(80,107,text='Name:   ', font=('Microsoft Yahei UI', 15, BOLD), fill='white')
mycanva.create_text(80,150,text='DOB:   ', font=('Microsoft Yahei UI', 15, BOLD), fill='white')
cal = DateEntry(mycanva, selectmode='day')
cal.grid(row=1, column=1, padx=15)
cal.place(x=160, y=140)
xysss = cal.get_date()

#==============================Submit Button======================
n = Button(xyz, text='Submit', padx=15, pady=8, command=HOROSCOPE)
n.place(x=170, y=200)



xyz.mainloop()