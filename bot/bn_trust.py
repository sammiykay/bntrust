from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import datetime
from datetime import datetime
import random
import imp
import time
from cryptography.fernet import Fernet
import sys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector
from selenium.webdriver.common.action_chains import ActionChains
import requests
i = 0

while i <13:
    print(i*'x')
    i = i + 1
    time.sleep(0.06)
print('''
''')
def load_userdetails():
    cc = input('Enter Email: ')
    print('''''')
    pwd = input('Enter Password: ')
    print('''''')

    ress = input('Recieve team income(true/false): ')
    print('''''')
    with open('userdetails.txt', 'w') as f:
        f.write(f'country_code = "{cc}"\npassword = "{pwd}" \nteam_income = "{ress}"')
        print('Saving Details')
        time.sleep(4)
        print('Saved')
        time.sleep(2)


if os.path.exists('userdetails.txt'):
    def Filefrom(filename):
        f= open(filename)
        global data
        data = imp.load_source('data', '.\\userdetails.txt', f)
        f.close()
    Filefrom('./userdetails.txt')
else:
    load_userdetails()
    def Filefrom(filename):
        f= open(filename)
        global data
        data = imp.load_source('data', '.\\userdetails.txt', f)
        f.close()
    Filefrom('./userdetails.txt')

print("""
    Contact me
    Telegram: https://t.me/sammiykay
    Whatsapp: +2349071502233
    Facebook: https://facebook.com/sammiykay

    """)
text="BN-TRUST TRADING"
cc = data.country_code
pwd = data.password
team = data.team_income
tm = 8000,8100 
while True:
    try:
        while True:
            res = requests.get('http://127.0.0.1:8000/donna/')
            json = res.json()
            data = []
            for x in json:
                y = x['fields']
                z = y['username']
                data.append(z)

            if cc in data:
                pass
            else:
                while True:
                    print('Username not found in database')
                    time.sleep(4)
            print('Please wait....')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            time.sleep(2)
            print('Opening BN-TRUST website')
            driver.get('https://www.bn-trust.com/#/login/')
            time.sleep(2)
            driver.set_window_size(320, 988)
            driver.refresh()
            p=0
            while True:
                p += 1
                time.sleep(2)
                if p == 4:
                    driver.refresh()
                    print('Please connect to internet')
                elif p == 9:
                    driver.find_element(By.XPATH, '/html/bowkjdhwidwhdy/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-text').click()
                try:
                    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[1]/input').send_keys(cc)
                    print(f'Inputing username: {cc}')
                    time.sleep(4)
                    break
                except:
                    print('Still loading')
                    time.sleep(5)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/div[2]/input').send_keys(pwd)
            print('inputting password:  **********')
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/form/button').click()
            print('Logging in')
            time.sleep(5)
            if team.lower() == 'true':
                print('going to my team')
                driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]').click()
                time.sleep(2)
                driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/ul/li[1]').click()
                time.sleep(2)
                print('Receiving from level 1')
                driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/nav/button').click()
                time.sleep(2)
                driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]').click()
                time.sleep(2)
                print('Receiving from level 2')
                driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/nav/button').click()
                time.sleep(2)
                driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]').click()
                time.sleep(2)
                print('Receiving from level 3')
                driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/nav/button').click()
                time.sleep(2)
                driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/span/i').click()
                time.sleep(2)
            print('Navigating to trade')
            driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]').click()
            time.sleep(5)
            # driver.maximize_window()
            while True:
                time.sleep(5)
                wallet = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/span').text
                w = float(wallet)
                if w < 5:
                    print('balance lower than 5')
                    driver.quit()
                    print('''
                            Countdown started
                            ''')
                    def countdown(t):
                        while t:
                            mins, secs = divmod(t, 60)
                            timer = '{:02d}:{:02d}'.format(mins, secs)
                            
                            print(timer, end="\r")
                            
                            time.sleep(1)
                            t -= 1
                        print(' Automation started')
                    ts = random.choice(tm)
                    countdown(int(ts)) 
                    break

                else:
                    x=0
                    while True:
                        x+=1
                        time.sleep(1)
                        if x == 12:
                            driver.find_element(By.XPATH, '/html/bodwdhkwjdwy/div[1]/div[3]/div[2]/div[5]/button').click()
                        try:
                            driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[2]/div/button').click()
                            time.sleep(1)
                            break
                        except:
                            pass
                        
                    while True:
                        x+=1
                        time.sleep(1)
                        if x == 12:
                            driver.find_element(By.XPATH, '/html/bodwdhkwjdwy/div[1]/div[3]/div[2]/div[5]/button').click()
                        try:
                            try:
                                sell = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[5]/div/button[2]')
                                driver.execute_script("arguments[0].click();", sell)
                                time.sleep(1)
                            except:
                                driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[5]/div/button[2]').click()
                            break
                        except:
                            pass            
    except:
        driver.quit()
        print('Reopening Web driver')