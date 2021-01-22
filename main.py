from selenium import webdriver
PATH = "C:/Python39/Scripts/chromedriver.exe"

driver = webdriver.Chrome(PATH)

#driver.get("https://www.offensive-security.com/")
driver.get("https://pastebin.com/")

print(driver.title)

