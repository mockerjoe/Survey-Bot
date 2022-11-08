from selenium import webdriver
import time
import subprocess
import tkinter as tk
from tkinter import *
from tkinter import ttk

def executeBot():
	file = open('combolist.txt')
	content = file.readlines()

	tries = int(test.get())
	timer = int(delay.get())

	line = 0

	while line < tries:
		# Import driver & open URL
		driver = webdriver.Firefox(executable_path=r"C:\Users\Jannik\Desktop\Jannik usb\Python-Programme\Survey-bot\geckodriver.exe")
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
		searchButton.click()
		time.sleep(timer)
		#--------------------------------------------------------------------------------------------------------------------------------------
		subprocess.call("TASKKILL /F /IM firefox.exe", shell=True)
		#subprocess.call("TASKKILL /F /IM geckodriver.exe", shell=True)
		#--------------------------------------------------------------------------------------------------------------------------------------
		line += 1

# Create Window
root = Tk()
root.title("Survey Bot  v0.2")
root.geometry("400x200")
root.resizable(False, False)

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
startButton = ttk.Button(root, text="Start", command=executeBot).place(x=170, y=150)

# Run window
root.mainloop()