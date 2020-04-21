import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

def yeet(countryLabelans, cases, lastupdated, deaths2, speed):
    find(countryLabelans, cases, lastupdated, deaths2, speed)

def find(countryLabelans, collectcases, lastupdated, deaths2, speed):

    try:

        URL = "https://www.worldometers.info/coronavirus/country/singapore/"

        headers = {
            "User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
            }

        page = requests.get(URL, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        cases = soup.find(id="maincounter-wrap").find("div", {"class": "maincounter-number"}).span.get_text()
        update = soup.find("div", {"style": "font-size:13px; color:#999; text-align:center"}).get_text()

        oof = cases
        oof2 = update

        countryLabelans.config(text="Singapore")
        collectcases.config(text=oof)
        lastupdated.config(text=oof2)

    except:
        speed += 1
        print("No Internet Connection! (",speed,")")

root = Tk()

root.title("Covid-19 Tracker")
root.resizable(False, False)

root.config(bg="white")

lastupdated = Label(root, text="", bg="white", fg="black", font=("calibri", 10))
lastupdated.pack(pady=10)

load = Image.open("covid-19.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render, bg="white")
img.pack()

countryFrame = Frame(root, bg="white")
countryFrame.pack(pady=15)
countryLabel = Label(countryFrame, text="Country", font=("Calibri", 15, 'bold'), bg="white", fg="#c70000")
countryLabel.pack()
countryLabelans = Label(countryFrame, text="", font=("Calibri", 20), fg="black", bg="white")
countryLabelans.pack()

casesLabel = Label(root, text="Cases", font=("Calibri", 15, 'bold'), bg="white", fg="#c70000")
casesLabel.pack()
cases = Label(root, text="", font=("Calibri", 20), fg="black", bg="white")
cases.pack()

speed = 0

Label(root, bg="white").pack(pady=5)

casesLabel.after(1, lambda:yeet(countryLabelans, cases, lastupdated, countryFrame, speed))

root.mainloop()
