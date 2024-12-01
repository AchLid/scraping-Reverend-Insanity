from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="D:\Desktop\ScrapRI\.venv\chromedriver.exe")
driver = webdriver.Chrome(service=service)

url = 'https://ar-no.com/novel/%d8%a7%d9%84%d9%82%d8%b3-%d8%a7%d9%84%d9%85%d8%ac%d9%86%d9%88%d9%86/'
driver.get(url)

def closeActive():
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/div[contains(@class, 'readmore')]/span[contains(@class,'chapter-readmore')]"))
    )
    Freadmore = driver.find_element(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/div[contains(@class, 'readmore')]/span[contains(@class,'chapter-readmore')]")
    Freadmore.click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][1]"))
    )
    Freadless = driver.find_element(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][1]")
    driver.execute_script("arguments[0].click();", Freadless)
    time.sleep(1)

def getDescription():
    WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//span[@class='btn btn-link content-readmore less']"))
    )
    Dreadmore = driver.find_element(By.XPATH, "//span[@class='btn btn-link content-readmore less']")
    Dreadmore.click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='description-summary']/div[@class='summary__content show-more active']/p"))
    )
    time.sleep(5)
    description_elements = driver.find_elements(By.XPATH, "//div[@class='description-summary']/div[@class='summary__content show-more active']/p")
    description = "\n".join([element.text for element in description_elements])
    with open("D:/Desktop/ScrapRI/Reverend Insanity/description.txt", 'w', encoding='utf-8') as f:
        f.write(description)
    print("Description saved successfully")

def getPartOneLinks():
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][6]"))
    )
    P1readmore = driver.find_element(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][6]")
    P1readmore.click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][6]/ul/li/ul/li/a"))
    )
    P1links = driver.find_elements(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][6]/ul/li/ul/li/a")
    P1links = P1links[::-1]
    with open("D:/Desktop/ScrapRI/Reverend Insanity/P1links.txt", 'w', encoding='utf-8') as f:
        for P1link in P1links:
            f.write(P1link.get_attribute('href')+"\n")
    driver.execute_script("arguments[0].click();", P1readmore)
    print("Folder one links saved successfully")
    time.sleep(1)

def getPartTwoLinks():
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][5]"))
    )
    P2readmore = driver.find_element(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][5]")
    P2readmore.click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][5]/ul/li/ul/li/a"))
    )
    P2links = driver.find_elements(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][5]/ul/li/ul/li/a")
    P2links = P2links[::-1]
    with open("D:/Desktop/ScrapRI/Reverend Insanity/P2links.txt", 'w', encoding='utf-8') as f:
        for P2link in P2links:
            f.write(P2link.get_attribute('href')+"\n")
    driver.execute_script("arguments[0].click();", P2readmore)
    print("Folder two links saved successfully")
    time.sleep(1)

def getPartThreeLinks():
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][4]"))
    )
    P3readmore = driver.find_element(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][4]")
    P3readmore.click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][4]/ul/li/ul/li/a"))
    )
    P3links = driver.find_elements(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][4]/ul/li/ul/li/a")
    P3links = P3links[::-1]
    with open("D:/Desktop/ScrapRI/Reverend Insanity/P3links.txt", 'w', encoding='utf-8') as f:
        for P3link in P3links:
            f.write(P3link.get_attribute('href')+"\n")
    driver.execute_script("arguments[0].click();", P3readmore)
    print("Folder three links saved successfully")
    time.sleep(1)

def getPartFourLinks():
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][3]"))
    )
    P4readmore = driver.find_element(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][3]")
    P4readmore.click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][3]/ul/li/ul/li/a"))
    )
    P4links = driver.find_elements(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][3]/ul/li/ul/li/a")
    P4links = P4links[::-1]
    with open("D:/Desktop/ScrapRI/Reverend Insanity/P4links.txt", 'w', encoding='utf-8') as f:
        for P4link in P4links:
            f.write(P4link.get_attribute('href')+"\n")
    driver.execute_script("arguments[0].click();", P4readmore)
    print("Folder four links saved successfully")
    time.sleep(1)

def getPartFiveLinks():
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][2]"))
    )
    P5readmore = driver.find_element(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][2]")
    P5readmore.click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][2]/ul/li/ul/li/a"))
    )
    P5links = driver.find_elements(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][2]/ul/li/ul/li/a")
    P5links = P5links[::-1]
    with open("D:/Desktop/ScrapRI/Reverend Insanity/P5links.txt", 'w', encoding='utf-8') as f:
        for P5link in P5links:
            f.write(P5link.get_attribute('href')+"\n")
    driver.execute_script("arguments[0].click();", P5readmore)
    print("Folder five links saved successfully")
    time.sleep(1)

def getPartSixLinks():
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][1]"))
    )
    P6readmore = driver.find_element(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][1]")
    P6readmore.click()
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][1]/ul/li/ul/li/a"))
    )
    P6links = driver.find_elements(By.XPATH, "//div[contains(@class, 'listing-chapters_wrap')]/ul/li[contains(@class, 'parent has-child')][1]/ul/li/ul/li/a")
    P6links = P6links[::-1]
    with open("D:/Desktop/ScrapRI/Reverend Insanity/P6links.txt", 'w', encoding='utf-8') as f:
        for P6link in P6links:
            f.write(P6link.get_attribute('href')+"\n")
    driver.execute_script("arguments[0].click();", P6readmore)
    print("Folder six links saved successfully")
    time.sleep(1)

closeActive()
getPartOneLinks()
getPartTwoLinks()
getPartThreeLinks()
getPartFourLinks()
getPartFiveLinks()
getPartSixLinks()
driver.quit()