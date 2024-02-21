import time 
import random
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver=webdriver.Chrome()

link="https://docs.google.com/forms/d/e/1FAIpQLSfbDae8hZ-HnGO3dKab0Y_ZID_NfvCCHT-ZPy1onS7TfsNgbg/viewform"
driver.get(link)

count=0


def q_auto():    
    gender_opt=random.choice([5,8,11])
    gen_path=   f'//*[@id="i{gender_opt}"]/div[3]/div'
    gender = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, gen_path)))
    gender.click()
    
    
    age_opt=random.choice([18,21,24,27,30])
    age_path=   f'//*[@id="i{age_opt}"]/div[3]/div'
    age = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, age_path)))
    age.click()
    
    
    income_opt=random.choice([37,40,43,46,49])
    income_path=   f'//*[@id="i{income_opt}"]/div[3]/div'
    income = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, income_path)))
    income.click()
    
    
    edu_opt=random.choice([56,59,62,65,68])
    edu_path=   f'//*[@id="i{edu_opt}"]/div[3]/div'
    edu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, edu_path)))
    edu.click()
    
    frq_opt=random.choice([72,75,78,81,84])
    frq_path=   f'//*[@id="i{frq_opt}"]/div[3]/div'
    frq = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, frq_path)))
    frq.click()
    
    awr_opt=random.choice([91,94,97,100])
    awr_path=   f'//*[@id="i{awr_opt}"]/div[3]/div'
    awr = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, awr_path)))
    awr.click()
    
    q_count_1=8
    while(q_count_1<24):
        opt = random.randint(1, 5)
        radio_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{q_count_1}]/div/div/div[2]/div/span/div/label[{opt}]/div[2]/div/div/div[3]/div'
        radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, radio_xpath)))
        radio.click()
        q_count_1=q_count_1+1

    q_count_2=25
    while(q_count_2<29):
        opt = random.randint(1, 5)
        radio_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{q_count_2}]/div/div/div[2]/div/span/div/label[{opt}]/div[2]/div/div/div[3]/div'
        radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, radio_xpath)))
        radio.click()
        q_count_2=q_count_2+1        
    
    q_count_3=30
    while(q_count_3<34):
        opt = random.randint(1, 5)
        radio_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{q_count_3}]/div/div/div[2]/div/span/div/label[{opt}]/div[2]/div/div/div[3]/div'
        radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, radio_xpath)))
        radio.click()
        q_count_3=q_count_3+1



while(count<25):

    q_auto()
    time.sleep(1)
    submit=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span')
    submit.click()
    count=count+1 
    
    driver.get(link)