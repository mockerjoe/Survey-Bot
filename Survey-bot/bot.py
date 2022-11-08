from selenium import webdriver
import time
import re

#import driver & open URL
driver = webdriver.Firefox(executable_path=r"C:\Users\Jannik\Desktop\Jannik usb\Python-Programme\Survey-bot\geckodriver.exe")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfdSY_UiBNthf9wZh3TNghWABWVYwRho6viZgHvGn0JwblI1w/viewform")

#test = "pimmelnase"

# open the sample file used
file = open('combolist.txt')
  
content = file.readlines()
line = 9

#open browser insert line
searchbox = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
searchbox.send_keys(content[line])

#click checkbox
checkBox = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div/div[3]/div')
checkBox.click()

#press search button
searchButton = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span/span')
#searchButton.click()

#open file, determine line
#file = open('combolist.txt')
#content = file.readlines()
#line = 0
#while line < 1:
#	print(content[line])
#	line = line + 1


#printline = 2
#lineCounter = 0
#with open('combolist.txt','r') as f:
#    for line in f:
#        lineCounter += 1
#        if lineCounter == printline:
#            print(line, end='')