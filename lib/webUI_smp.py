import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import SMP_URL_LOGIN


class SMP_UI:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.wd = webdriver.Chrome(options=options)
        self.wd.implicitly_wait(10)

    def login(self, username, password):
        self.wd.get(SMP_URL_LOGIN)
        time.sleep(2)
        if username is not None:
            self.wd.find_element(By.ID, 'username').send_keys(username)
        if password is not None:
            self.wd.find_element(By.ID, 'password').send_keys(password)
        time.sleep(2)
        self.wd.find_element(By.ID, 'loginBtn').click()

sampUi = SMP_UI()