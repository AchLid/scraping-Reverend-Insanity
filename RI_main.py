import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def getChapterLink():
    chapter_num = int(input("what chapter do you want to read: "))
    if 1<=chapter_num<=199:
        file = "P1links.txt"
        x = 0
    elif 200<=chapter_num<=405:
        file = "P2links.txt"
        x = 199
    elif 406<=chapter_num<=649:
        file = "P3links.txt"
        x = 405
    elif 650<=chapter_num<=1021:
        file = "P4links.txt"
        x = 649
    elif 1022<=chapter_num<=1966:
        file = "P5links.txt"
        x = 1021
    elif 1967<=chapter_num<=2334:
        file = "P6links.txt"
        x = 1966
    else:
        print("Not a valid chapter")
    with open(f"D:/Desktop/ScrapRI/Reverend Insanity/{file}", 'r') as f:
        links = f.readlines()
    return links[chapter_num-x-1]

def getTittle():
    chapterLink = getChapterLink()
    service = Service(executable_path="D:\Desktop\ScrapRI\.venv\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    url = chapterLink
    driver.get(url)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='text-left']/p"))
    )
    tittle = driver.find_element(By.XPATH, "//div[@class='text-left']/p[1]").text
    with open("D:/Desktop/ScrapRI/Reverend Insanity/tittle.txt", 'w', encoding='utf-8') as f:
        f.write(tittle)
    print("Tittle saved successfully")
    driver.quit()

def openChapter():
    chapterLink = getChapterLink()
    webbrowser.open_new(chapterLink)
