from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import random
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
	# file = open('combolist.txt')
	# content = file.readlines()

	# content2 = random.choice(open("combolist.txt","r").readlines())
	# #print(content2)
	# len_mail = (len(content2))

	# try:
	# 	tries = int(test.get())
	# except:
	# 	print("Gibt eine ganze Zahl für die Versuche ein.")
	
	# try:
	# 	timer = int(delay.get())
	# except:
	# 	print("Gib eine Anzahl der Sekunden für einen verzögerten Input ein")

	# Get Tries and Delay from Window
	tries = int(mail.get())
	timer = int(delay.get())


	# while line < tries:
	# 	# Import driver & open URL
	# 	if is_on == True:
	# 		driver = webdriver.Firefox(executable_path=r"C:\Users\Jannik\Desktop\Jannik usb\Python-Programme\Survey-bot\geckodriver.exe") # Change path from "C to \
	# 	else:
	# 		driver = webdriver.Chrome(executable_path=r"C:\Users\Jannik\Desktop\Jannik usb\Python-Programme\Survey-bot\chromedriver.exe") # Change path from "C to \
		
	# 	driver.get("https://docs.google.com/forms/d/e/1FAIpQLSearfedPRO3B7ivKgiz_R0sAY0Q79l3dF836tb5UD-a3pMnaw/viewform") # Insert Link of Google Survey
	# 	#--------------------------------------------------------------------------------------------------------------------------------------
	# 	time.sleep(timer)
	# 	#--------------------------------------------------------------------------------------------------------------------------------------
	# 	# Open browser insert line
	# 	#searchbox = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
	# 	searchbox = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
	# 	searchbox.send_keys(content2[line])
	# 	#--------------------------------------------------------------------------------------------------------------------------------------
	# 	time.sleep(timer)
	# 	#--------------------------------------------------------------------------------------------------------------------------------------
	# 	# Click checkbox
	# 	#checkBox = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
	# 	checkBox = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
	# 	checkBox.click()
	# 	#--------------------------------------------------------------------------------------------------------------------------------------
	# 	time.sleep(timer)
	# 	#--------------------------------------------------------------------------------------------------------------------------------------
	# 	# Press search button
	# 	#searchButton = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
	# 	searchButton = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
	# 	#searchButton.click()
	# 	time.sleep(timer)
	# 	#--------------------------------------------------------------------------------------------------------------------------------------
	# 	driver.close()
	# 	driver.quit()
	# 	#--------------------------------------------------------------------------------------------------------------------------------------
	# 	line += 1

	while tries > 0:
		# Choose random Mail from Combolist
		content2 = random.choice(open("combolist.txt","r").readlines())
		#print(content2)
		len_mail = (len(content2))

		# Set range for random delay
		rand_time = random.randrange(0,timer)
		print(rand_time)

		# Import driver & open URL
		if is_on == True:
			driver = webdriver.Firefox(executable_path=r"C:\Users\Jannik\Desktop\Jannik usb\Python-Programme\Survey-bot\geckodriver.exe") # Change path from "C to \
		else:
			driver = webdriver.Chrome(executable_path=r"C:\Users\Jannik\Desktop\Jannik usb\Python-Programme\Survey-bot\chromedriver.exe") # Change path from "C to \
		
		driver.get("https://docs.google.com/forms/d/e/1FAIpQLSearfedPRO3B7ivKgiz_R0sAY0Q79l3dF836tb5UD-a3pMnaw/viewform") # Insert Link of Google Survey
		#--------------------------------------------------------------------------------------------------------------------------------------
		time.sleep(rand_time)
		#--------------------------------------------------------------------------------------------------------------------------------------
		# Open browser insert line
		#searchbox = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
		searchbox = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
		searchbox.send_keys(content2[0:len_mail])
		#--------------------------------------------------------------------------------------------------------------------------------------
		time.sleep(rand_time)
		#--------------------------------------------------------------------------------------------------------------------------------------
		# Click checkbox
		#checkBox = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
		checkBox = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
		checkBox.click()
		#--------------------------------------------------------------------------------------------------------------------------------------
		time.sleep(rand_time)
		#--------------------------------------------------------------------------------------------------------------------------------------
		# Press search button
		#searchButton = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
		searchButton = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
		searchButton.click()
		time.sleep(rand_time)
		#--------------------------------------------------------------------------------------------------------------------------------------
		driver.close()
		driver.quit()
		#--------------------------------------------------------------------------------------------------------------------------------------
		tries -= 1

# Create Window
root = Tk()
root.title("Survey Bot  v0.4.4")
root.geometry("368x368")
root.resizable(False, False)

# Window background image
bgimg= tk.PhotoImage(file = "Assets/schmaettingx2.png")
limg= Label(root, i=bgimg)
limg.pack()

# Set icon for window
root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(file="Assets/mr_bot.png"))

# Assign Swith Images
on = PhotoImage(file = "Assets/on.png")
off = PhotoImage(file = "Assets/off.png")

# Create A Button
switch = Button(root, image = on, bd = 0, command = driverSwitch)
switch.place(x=140,y=90)

# Label for Switch
tk.Label(root, text="Firefox").place(x=243,y=101)
tk.Label(root, text="Chrome").place(x=90,y=101)

# Create User Input 
tk.Label(root, bd = 0,text="Anzahl der versuchten Mails").place(x=20,y=20)
tk.Label(root, bd = 0,text="Delay Obergrenze in Sekunden").place(x=20,y=55)
mail = Entry(root)
mail.place(x=225,y=20)
delay = Entry(root)
delay.place(x=225,y=55)

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
startButton.place(x=155, y=150)

# Run window
root.mainloop()
