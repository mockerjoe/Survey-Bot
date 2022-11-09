from selenium import webdriver
import time
import subprocess
import tkinter as tk
from tkinter import *
from tkinter import ttk

# def selectDriver():
# 	global var1, var2, driver
# 	# Select Browser Driver
# 	if(var1.get() == 0) & (var2.get() == 0):
# 		print()
# 	elif(var1.get() == 1) & (var2.get() == 0):
# 		driver = webdriver.Firefox(executable_path=r"C:\Users\Jannik\Desktop\Jannik usb\Python-Programme\Survey-bot\geckodriver.exe")
# 		return driver
# 		#var2 = 0
# 	elif(var1.get() == 0) & (var2.get() == 1):
# 		driver = webdriver.Chrome(executable_path=r"C:\Users\Jannik\Desktop\Jannik usb\Python-Programme\Survey-bot\chromedriver.exe")
# 		return driver
# 	else:
# 		return driver

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
		# Import driver & open URL
		if is_on == True:
			driver = webdriver.Firefox(executable_path=r"C:\Users\Jannik\Desktop\Jannik usb\Python-Programme\Survey-bot\geckodriver.exe") # Change path from "C to \
		else:
			driver = webdriver.Chrome(executable_path=r"C:\Users\Jannik\Desktop\Jannik usb\Python-Programme\Survey-bot\chromedriver.exe") # Change path from "C to \
		
		driver.get("https://docs.google.com/forms/d/e/1FAIpQLSearfedPRO3B7ivKgiz_R0sAY0Q79l3dF836tb5UD-a3pMnaw/viewform") # Insert Link of Google Survey
		#--------------------------------------------------------------------------------------------------------------------------------------
		time.sleep(timer)
		#--------------------------------------------------------------------------------------------------------------------------------------
		# Open browser insert line
		searchbox = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
		searchbox.send_keys(content[line])
		#--------------------------------------------------------------------------------------------------------------------------------------
		time.sleep(timer)
		#--------------------------------------------------------------------------------------------------------------------------------------
		# Click checkbox
		checkBox = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
		checkBox.click()
		#--------------------------------------------------------------------------------------------------------------------------------------
		time.sleep(timer)
		#--------------------------------------------------------------------------------------------------------------------------------------
		# Press search button
		searchButton = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
		searchButton.click()
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

# # Initialize Checkbox variables
# var1 = tk.IntVar()
# var2 = tk.IntVar()

# # Create Checkbox
# ff = Checkbutton(root, text='Firefox', onvalue=1, offvalue=0, command=selectDriver)
# ff.place(x=75,y=100)
# ch = Checkbutton(root, text='Chome', onvalue=1, offvalue=0, command=selectDriver)
# ch.place(x=275,y=100)

# Button for execute
startButton = ttk.Button(root, text="Start", state=NORMAL, command=executeBot)
startButton.place(x=160, y=150)

# Run window
root.mainloop()
