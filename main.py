import time
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
driver = webdriver.Chrome()

link = "https://docs.google.com/forms/d/e/1FAIpQLSfbDae8hZ-HnGO3dKab0Y_ZID_NfvCCHT-ZPy1onS7TfsNgbg/viewform"
driver.get(link)

count = 0

while(count < 25):
    try:
        # Wait for the submit button to be clickable, then click
        # submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')))
        # submit.click()
        
        # # Wait for the radio button to be clickable, then click
        # radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div')))
        # radio.click()
        
        # radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div')))
        # radio.click()
        
        # //*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div

        # radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i5"]/div[3]/div')))
        # radio.click()
        
        
        q_count_1=8
        while(q_count_1<24):
            # opt = random.randint(1,5)
            # xpath=f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{q_count}]]/div/div/div[2]/div/span/div/label[{opt}]/div[2]/div/div/div[3]/div'
            # radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            # radio.click()
        
            opt = random.randint(1, 5)
            radio_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{q_count_1}]/div/div/div[2]/div/span/div/label[{opt}]/div[2]/div/div/div[3]/div'
            radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, radio_xpath)))
            radio.click()
            q_count_1=q_count_1+1

            # //*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div
            # //*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div


            # //*[@id="mG61Hd"]/div[2]/div/div[2]/div[25]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div/div
            # //*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div
        
        
        q_count_2=25
        
        while(q_count_2<29):
            
        
        
        
        
        
        
        
        
        
        
        
        
        time.sleep(1)  # Adjust sleep as necessary for the page to load/submit
        driver.get(link)
    except Exception as e:
        print(f"Encountered an exception: {e}")
        break  # Exit the loop if there's an error
    count += 1

# Keep the browser open until the user decides to close it
input("Press Enter to close...")
driver.quit()
