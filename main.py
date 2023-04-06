import time
import json
import pyautogui
from random import choice
from json import load
from typing import Any
from contextlib import suppress
import chromedriver_autoinstaller
from pynput.mouse import Controller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from pynput.keyboard import Key, Controller
from fake_useragent import UserAgent


class mailGen:
    def __init__(self):
        self.config: Any = load(open('config.json'))
        self.driver = None
        self.email = ""
        self.password = ""
        self.width = ""
        self.height = ""
        self.proxies = [i.strip() for i in open(self.config['Common']['ProxyFile']).readlines()]
   
    def GetMailInfo(self):
        url = 'https://gmail30min.com/api/san-pham/mua2?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNDQ3MDY2Y2ZjOTU0NGJhMGNhZTI1MDc3ODg5M2M4Y2UxMTY5MzQ3Yzk5MzFlYWUwNTIwN2Y1MzhkMDE0MWVlNzQzNWM2YzFlZWQwMmQ0NDEiLCJpYXQiOjE2Nzg4OTQ4MzguMjU3NDI0LCJuYmYiOjE2Nzg4OTQ4MzguMjU3NDMxLCJleHAiOjE3MTA1MTcyMzguMjU0MTM0LCJzdWIiOiI2OTUiLCJzY29wZXMiOltdfQ.qWtzKo8m_jlRatH5kiFXNcfkv6zV3x7_r8t6No7DHsbPPDnGSTAHsPAD9QhSJarw5tUzCKuEIBKi-iDacQgkvA6yyv3Fi6_iz_f-aNxTfD71xXbWIB1F9RgKeMd7Sqg8aIcv8opq7OawADiKa50ln1yGrgpZeXp046MHyducqk7adJDsYkXjk5UJltOyTykJWn_e6kOrr1wNMAvGh4QBiPWcew-t7Hlg1NHhzO36FvU4DRaW4GoGh4XBjpH2LO5KLLNBb9Ldjj4MFl-S7zuw05aTBtki6Egn8WS2Q3viyZNclE_2GhYk7a87Le4fPwyQIQlfACbgF9KcZvmaj3Z8EDQ-ufXBYjpXtlW1pEuUovVI1yKziOl7Ip7FdL_XoG4sHUu3oprbjMWKXrUXI7SQC-bfSzMtR6h2-XhsutWZIu4SIZ6DR-t1XENDkBwLZh6nCB4X3Zzw-v1R2Txz62SIqO-3X-c4uFryw4ko6XVl44wOAa9GQiB14sE2sCKOSHI3KUBRgLxuUWBouS2UtSsrkYOl7UDlhTTi7dFc-XLv8ouJEWdxLdENwmCkrcPYOj-l3ZK-3nIgpqCobFJhFW1VuYvlezVe6iAwlamDZTBF2M4NcK0YazNmuJgaioBNnBcm3VdGW1-HUrPrjIpJ6hkELOzHYBivO2PX3REVrqPGErw&quantity=1&category=12&fbclid=IwAR1AOXuxeUaUocnpZIWlrgTlIqThF2J7WWdNHHFRpAX1mwu0xDNfLU7-Eyo'
        self.driver.get(url)
        email_tag = self.driver.find_element(By.XPATH, '/html/body/pre')
        json_data = json.loads(email_tag.text)
        data = json_data['success']['products']
        self.email = data[0].split('|')[0]
        self.password = data[0].split('|')[1]
    def Google(self):
        self.driver.get('https://accounts.google.com')
        self.driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(self.email)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
        time.sleep(5)
        self.SignInTextNow()
    def SignInTextNow(self):
        keyboard = Controller()

        self.width = self.driver.execute_script("return window.innerWidth;")
        self.height = self.driver.execute_script("return window.innerHeight;")

        textnow_url = 'https://www.textnow.com/login'
        self.driver.execute_script("window.open('about:blank','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(textnow_url)

        time.sleep(3.5)
        self.driver.find_element_by_xpath('//*[@id="google-auth-btn"]').click()
        time.sleep(5)
        keyboard.type(self.email)
        keyboard.press(Key.enter)
        time.sleep(3.5)
        keyboard.type(self.password)
        keyboard.press(Key.enter)
        time.sleep(5)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(1)
        keyboard.press(Key.enter)
        time.sleep(5)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(2)
        element = self.driver.find_element_by_css_selector('#px-captcha')
        action = ActionChains(self.driver)
        action.click_and_hold(element)
        action.perform()
        time.sleep(10)
        action.release(element)
        action.perform()
        time.sleep(0.2)
        action.release(element)
        time.sleep(10)

    def SetProxyOption(self):
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
            self.driver.maximize_window()

    def run(self):
       self.SetProxyOption()
       self.GetMailInfo()
    #    self.Google()
       self.SignInTextNow()

if __name__ == '__main__':
    mailGen().run()