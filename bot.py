from selenium import webdriver
import time
import subprocess
import tkinter as tk
from tkinter import *
from tkinter import ttk

is_on = True

def driverSwitch():
	global is_on

	if is_on:
		switch.config(image=off)
		is_on = False
	else:
		switch.config(image=on)
		is_on = True

def executeBot():
	file = open('combolist.txt')
	content = file.readlines()
	
	tries = int(test.get())
	timer = int(delay.get())

	line = 0

	while line < tries:
		# Import driver
		if is_on == True:
			driver = webdriver.Firefox(executable_path=r"C:\Users\Jannik\Desktop\Jannik usb\Python-Programme\Survey-bot\geckodriver.exe") # Change path from "C to \
		else:
			driver = webdriver.Chrome(executable_path=r"C:\Users\Jannik\Desktop\Jannik usb\Python-Programme\Survey-bot\chromedriver.exe") # Change path from "C to \

		# Open URL
		driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfdSY_UiBNthf9wZh3TNghWABWVYwRho6viZgHvGn0JwblI1w/viewform")
		#--------------------------------------------------------------------------------------------------------------------------------------
		time.sleep(timer)
		#--------------------------------------------------------------------------------------------------------------------------------------
		# Open browser insert line
		searchbox = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
		searchbox.send_keys(content[line])
		#--------------------------------------------------------------------------------------------------------------------------------------
		time.sleep(timer)
		#--------------------------------------------------------------------------------------------------------------------------------------
		# Click checkbox
		checkBox = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div/div[3]/div')
		checkBox.click()
		#--------------------------------------------------------------------------------------------------------------------------------------
		time.sleep(timer)
		#--------------------------------------------------------------------------------------------------------------------------------------
		# Press search button
		searchButton = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span/span')
		#searchButton.click()
		time.sleep(timer)
		#--------------------------------------------------------------------------------------------------------------------------------------
		subprocess.call("TASKKILL /F /IM firefox.exe", shell=True)
		subprocess.call("TASKKILL /F /IM geckodriver.exe", shell=True)
		#--------------------------------------------------------------------------------------------------------------------------------------
		line += 1

# Create Window
root = Tk()
root.title("Survey Bot  v0.4")
root.geometry("400x200")
root.resizable(False, False)

# Set icon for window
root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(file="Assets/mr_bot.png"))

# Assign Swith Images
on = PhotoImage(file = "Assets/on.png")
off = PhotoImage(file = "Assets/off.png")

# Create A Button
switch = Button(root, image = on, bd = 0, command = driverSwitch)
switch.place(x=145,y=90)

# Label for Switch
tk.Label(root, text="Firefox").place(x=250,y=101)
tk.Label(root, text="Chrome").place(x=95,y=101)

# Create User Input 
tk.Label(root, text="Anzahl der versuchten Mails").place(x=30,y=20)
tk.Label(root, text="Delay in Sekunden").place(x=30,y=55)
test = Entry(root) #.place(x=230,y=20)
test.place(x=230,y=20)
delay = Entry(root) #.place(x=230,y=55)
delay.place(x=230,y=55)

file = open('combolist.txt')
content = file.readlines()

# Button for execute
startButton = ttk.Button(root, text="Start", command=executeBot).place(x=160, y=150)

# Run window
root.mainloop()