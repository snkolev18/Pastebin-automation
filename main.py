from selenium import webdriver
# keys will be used in order to type in text box
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

PATH = "C:/Python39/Scripts/chromedriver.exe"
driver = webdriver.Chrome(PATH)


def listToString(listInput):
    res = ""
    for element in listInput:
        if element != "#":
            res += element
            res += '\n'
    return res


print("Insert # if you want to stop. Type the code, that you want to be inputted: ")
userLines = []
while True:
    text_input = input()
    if text_input.strip() == "#":
        break
    userLines.append(text_input)

input_text = listToString(userLines)

driver.get("https://pastebin.com/")

print(driver.title)

textBox = driver.find_element_by_id("postform-text")
textBox.send_keys(input_text)
try:
    button_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
    button_element.click()
finally:
    time.sleep(5)
    print(driver.current_url)
    driver.quit()