from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="D:\Desktop\Scapy\.venv\chromedriver.exe")
driver = webdriver.Chrome(service=service)

url = 'https://ar-no.com/novel/%d8%a7%d9%84%d9%82%d8%b3-%d8%a7%d9%84%d9%85%d8%ac%d9%86%d9%88%d9%86/'
driver.get(url)

def saveDescription():
    WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//span[@class='btn btn-link content-readmore less']"))
    )
    readmore = driver.find_element(By.XPATH, "//span[@class='btn btn-link content-readmore less']")
    readmore.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='description-summary']/div[@class='summary__content show-more active']/p"))
    )
    time.sleep(5)
    description_elements = driver.find_elements(By.XPATH, "//div[@class='description-summary']/div[@class='summary__content show-more active']/p")
    description = "\n".join([element.text for element in description_elements])
    with open("D:/Desktop/Reverend Insanity/description.txt", 'w', encoding='utf-8') as f:
        f.write(description)
    print("File saved successfully")

saveDescription()

driver.quit()
