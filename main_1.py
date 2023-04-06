import requests
import time
import json
import random
import keyboard
import pyautogui
import chromedriver_autoinstaller 
from contextlib import suppress
from requests import get
from json import load
from typing import Any
from random import choice
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import seleniumwire.undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType


class mailGen:
    def __init__(self):
        self.config: Any = load(open('config.json'))
        self.driver = None
        self.email = ""
        self.password = ""
        self.proxies = [i.strip() for i in open(self.config['Common']['ProxyFile']).readlines()]
        print("called init function")

    def check_proxy(self, proxy):
        with suppress(Exception):
            proxies = {
            'http': f'{proxy}',
            'https': f'{proxy}'
            }
            response = requests.request(
                'GET',
                'https://shifter.io',
                proxies=proxies,
            )
            if response.status_code == 200:
                return True
        return False
    
    def fElement(self, driver, by: By = By.XPATH, value=None, delay: float = 0.3):
        # Custom find Element Function
        count = 0
        while count <= 100:
            with suppress(Exception):
                return driver.find_element(by, value)
            time.sleep(delay)
            count += 1
        print(f'tried 100 time to find element...')
        driver.quit()
        return
        
    def send_keys_delay(self, controller, keys, delay=0.1):
        for key in keys:
            if key == "@":
                # Press and hold the Shift key
                pyautogui.keyDown('shift')
                # Press the 2 key
                pyautogui.press('2')
                # Release the 2 key
                pyautogui.keyUp('2')
                # Release the Shift key
                pyautogui.keyUp('shift')
            else:
                keyboard.press_and_release(key)
        
            time.sleep(random.uniform(0,1))

    def CreateGoogleAcc(self, driver):
        try:
            url = 'https://accounts.google.com'
            self.driver.get(url)

            time.sleep(3.5)
            wait = WebDriverWait(driver, 3)
            email_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'))) 

            self.send_keys_delay(email_element,self.email)
            keyboard.press_and_release('enter')

            time.sleep(4.5)

            pass_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'))) 

            self.send_keys_delay(pass_element, self.password)
            keyboard.press_and_release('enter')


            time.sleep(2)
            wait = WebDriverWait(driver, 3)
            # input()

            time.sleep(5) 
            wait = WebDriverWait(driver, 5) 
            input()
            self.SignToTextNow(driver=self.driver)

        except Exception as e:
            if e == KeyboardInterrupt:
                driver.quit()
                exit(0)
            print("Something is wrong | %s" % str(e).split("\n")[0].strip())
            driver.quit()
            exit(0)
        finally:
            driver.quit()

    def SignToTextNow(self, driver):
        # try:
            textnow_url = 'https://www.textnow.com/signup'
            # driver.execute_script("window.open('about:blank','_blank');")
            # driver.switch_to.window(driver.window_handles[1])
            self.driver.get(textnow_url)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[3]/div[2]').click()
            time.sleep(3.5)
            driver.execute_script("window.open('about:blank','_blank');")
            driver.switch_to.window(driver.window_handles[1])
            self.driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S-1140697614%3A1680232669423720&continue=https%3A%2F%2Faccounts.google.com%2Fgsi%2Fselect%3Fclient_id%3D302791216486-uvga7gfpsv09349lkhe1c8rmg73of0h5.apps.googleusercontent.com%26ux_mode%3Dpopup%26ui_mode%3Dcard%26as%3DtHWcE9BNxlz09g15MXinxw%26channel_id%3Dbdde78a152fdb3c34a9c45ed9fa0c955b6264e4ff26d22c7ba2253a7e8b1bba2%26origin%3Dhttps%3A%2F%2Fwww.textnow.com&faa=1&ifkv=AQMjQ7RnlQTGQD5SECYicOP7_YpZWh7fo5okW9W8GYCtfvHS7TwLtMFzRrup58gQ7hmvmhY1kWmJVA&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(self.email)
            time.sleep(3.5)
            # self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(self.password)
            # # signup_google_button.click()
            # time.sleep(10)

        # except Exception as e:
        #     if e == KeyboardInterrupt:
        #         driver.quit()
        #         exit(0)
        #     print("Something is wrong | %s" % str(e).split("\n")[0].strip())
        #     driver.quit()
        #     exit(0)
        # finally:
        #     driver.quit()

    def GetMailInfo(self, driver):
        url = 'https://gmail30min.com/api/san-pham/mua2?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNDQ3MDY2Y2ZjOTU0NGJhMGNhZTI1MDc3ODg5M2M4Y2UxMTY5MzQ3Yzk5MzFlYWUwNTIwN2Y1MzhkMDE0MWVlNzQzNWM2YzFlZWQwMmQ0NDEiLCJpYXQiOjE2Nzg4OTQ4MzguMjU3NDI0LCJuYmYiOjE2Nzg4OTQ4MzguMjU3NDMxLCJleHAiOjE3MTA1MTcyMzguMjU0MTM0LCJzdWIiOiI2OTUiLCJzY29wZXMiOltdfQ.qWtzKo8m_jlRatH5kiFXNcfkv6zV3x7_r8t6No7DHsbPPDnGSTAHsPAD9QhSJarw5tUzCKuEIBKi-iDacQgkvA6yyv3Fi6_iz_f-aNxTfD71xXbWIB1F9RgKeMd7Sqg8aIcv8opq7OawADiKa50ln1yGrgpZeXp046MHyducqk7adJDsYkXjk5UJltOyTykJWn_e6kOrr1wNMAvGh4QBiPWcew-t7Hlg1NHhzO36FvU4DRaW4GoGh4XBjpH2LO5KLLNBb9Ldjj4MFl-S7zuw05aTBtki6Egn8WS2Q3viyZNclE_2GhYk7a87Le4fPwyQIQlfACbgF9KcZvmaj3Z8EDQ-ufXBYjpXtlW1pEuUovVI1yKziOl7Ip7FdL_XoG4sHUu3oprbjMWKXrUXI7SQC-bfSzMtR6h2-XhsutWZIu4SIZ6DR-t1XENDkBwLZh6nCB4X3Zzw-v1R2Txz62SIqO-3X-c4uFryw4ko6XVl44wOAa9GQiB14sE2sCKOSHI3KUBRgLxuUWBouS2UtSsrkYOl7UDlhTTi7dFc-XLv8ouJEWdxLdENwmCkrcPYOj-l3ZK-3nIgpqCobFJhFW1VuYvlezVe6iAwlamDZTBF2M4NcK0YazNmuJgaioBNnBcm3VdGW1-HUrPrjIpJ6hkELOzHYBivO2PX3REVrqPGErw&quantity=1&category=12&fbclid=IwAR1AOXuxeUaUocnpZIWlrgTlIqThF2J7WWdNHHFRpAX1mwu0xDNfLU7-Eyo'
        driver.get(url)
        email_tag = driver.find_element(By.XPATH, '/html/body/pre')
        json_data = json.loads(email_tag.text)
        data = json_data['success']['products']
        self.email = data[0].split('|')[0]
        self.password = data[0].split('|')[1]

    def run(self):
        with suppress(IndexError):
            proxy_ip_port = choice(self.proxies) #select proxy
            
            proxy = Proxy()
            proxy.proxy_type = ProxyType.MANUAL
            proxy.http_proxy = proxy_ip_port
            proxy.ssl_proxy = proxy_ip_port

            capabilities = webdriver.DesiredCapabilities.CHROME
            proxy.add_to_capabilities(capabilities)

            chromedriver_autoinstaller.install() 
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-blink-features=AutomationControlled") 
            options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
            options.add_experimental_option("useAutomationExtension", False) 
            options.add_argument('--proxy-server=%s' % proxy_ip_port)

            self.driver = webdriver.Chrome(options=options, desired_capabilities=capabilities)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

            # Initializing a list with two Useragents 
            useragentarray = [ 
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", 
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", 
            ] 
            # for i in range(len(useragentarray)): 
            #     self.driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": useragentarray[i]}) 
            #     print(self.driver.execute_script("return navigator.userAgent;")) 
            #     self.GetMailInfo(driver=self.driver)
            #     # self.CreateGoogleAcc(driver=self.driver)
            #     self.SignToTextNow(driver=self.driver)
            # self.driver.close()


            self.driver.maximize_window()
            # self.GetMailInfo(driver=self.driver)
            # self.CreateGoogleAcc(driver=self.driver)
            self.SignToTextNow(driver=self.driver)
            print(self.driver.get_window_size())
            print("start programe")

if __name__ == '__main__':
    mailGen().run()