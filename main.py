import os
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

query = input("Which customer's phone number would you like to find?: ").upper()
username = os.environ.get("username")
password = os.environ.get("pass")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url=f"{os.environ.get('website')}")


def login():
    pyautogui.typewrite(f"{username}")
    time.sleep(1)
    pyautogui.typewrite(['tab'])
    time.sleep(1)
    pyautogui.typewrite(f"{password}")
    time.sleep(1)
    pyautogui.typewrite(['enter'])
    time.sleep(2)


def save_report():
    save_location = pyautogui.locateOnScreen('save_button.png')
    save_center = pyautogui.center(save_location)
    pyautogui.click(save_center.x, save_center.y)
    time.sleep(1)
    pyautogui.typewrite(f"{query.title()} Report")
    pyautogui.typewrite(['enter'])
    time.sleep(3)


# requires twice login for selenium.
login()
login()
time.sleep(7)
driver.maximize_window()

spans = driver.find_elements(By.CSS_SELECTOR, "span")
for lab in spans:
    if query in lab.text:
        lab.click()
        break
instrument_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div["
                                                  "2]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div["
                                                  "3]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div["
                                                  "1]/div/div/div[2]/div/div/div[5]/div[3]/button")
instrument_button.click()
time.sleep(4)
insight_button = driver.find_element(By.XPATH, "/html/body/div[25]/div[2]/div/div[2]/div/div/div[2]/div/div["
                                               "2]/div/div/div/div/div/div[1]/div/div/div["
                                               "2]/div/div/div/div/div/div/ul/li[3]/table/tbody/tr/td/a")
insight_button.click()
time.sleep(4)
first_lot = driver.find_element(By.XPATH, "/html/body/div[25]/div[2]/div/div[2]/div/div/div[2]/div/div["
                                          "2]/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div["
                                          "2]/div/div/div[2]/div/div/div[1]/div/div/div/div/div["
                                          "1]/div/div/div/div/div[3]/div/div/div[2]/table/tbody/tr[2]")
first_lot.click()
view_report = driver.find_element(By.XPATH, "/html/body/div[25]/div[2]/div/div[2]/div/div/div[2]/div/div["
                                            "2]/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div["
                                            "2]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/div/div["
                                            "2]/div/div/div[1]/div[3]/button")
view_report.click()
time.sleep(3)
save_report()

print('File has been saved.')
