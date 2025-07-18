import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import pandas as pd
import time
from urllib.parse import quote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = os.path.join(os.getcwd(), "chromedriver.exe")
service = Service(CHROMEDRIVER_PATH, log_path=os.devnull)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=C:/Users/swast/whatsapp_profile")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://web.whatsapp.com")
input("Scan QR code and press Enter when ready...")


df = pd.read_csv("contacts.csv")
df.columns = df.columns.str.strip()
df['Phone'] = df['Phone'].astype(str) 


for idx, row in df.iterrows():
    phone = row['Phone'].replace(" ", "").replace("+", "")
    message = quote(str(row['Message']))
    url = f"https://web.whatsapp.com/send?phone={phone}&text={message}"

    driver.get(url)
    time.sleep(10)

    try:
        send_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send"]'))
        )
        send_button.click()
        print(f"[✓] Message sent to {row['Name']}")
    except Exception as e:
        print(f"[x] Failed to send message to {row['Name']}: {e}")
    
    time.sleep(5)

print("✅ All messages processed.")
driver.quit()
