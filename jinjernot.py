from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import webbrowser

print("Bienvenido a Jinjernot")
user = input("Ingresa el usuario a estalkear  ")

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(2)

#Log in

username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

username_input.send_keys("")
password_input.send_keys("")

login_link = browser.find_element("xpath", "//div[text()='Log In']")
login_link.click()

time.sleep(3)

#----
passlogin_link = browser.find_element("xpath", "//button[text()='Not Now']")
passlogin_link.click()

time.sleep(3)

passlogin_link = browser.find_element("xpath", "//button[text()='Not Now']")
passlogin_link.click()

time.sleep(3)

search_user = browser.find_element("xpath", "//input[@placeholder='Search']")
search_user.send_keys(user)
time.sleep(3)
search_user.send_keys(Keys.ENTER)
search_user.send_keys(Keys.ENTER)

time.sleep(3)

folder_name = user
folder = "im"
os.mkdir(folder_name)
os.mkdir(folder)

images = browser.find_elements(By.TAG_NAME,'img')

i=0
for x in images:
    ext = ".jpg"
    src = x.get_attribute("src")
    time.sleep(1)
    path = (f'{folder_name}/{folder_name}{i}{ext}')
    path2 = ((f'{folder}/{i}{ext}'))
    chida = urllib.request.urlretrieve(src, path)
    palreact = urllib.request.urlretrieve(src, path2)
    print(chida)
    print(palreact)
    i=i+1
browser.close()

webbrowser.open_new_tab('jinjernot.html')