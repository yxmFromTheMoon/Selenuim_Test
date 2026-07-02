import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

    def get_first_page_device_models(self):
        self.wd.implicitly_wait(10)
        values = self.wd.find_elements(By.CSS_SELECTOR, '.field-value')
        self.wd.implicitly_wait(10)
        deviceModels = []
        for idx, value in enumerate(values):
            if (idx + 1) % 3 == 0:
                deviceModels.append(
                    [values[idx - 2].text, values[idx - 1].text, values[idx].text]
                )
        return deviceModels

    def delete_first_item(self) -> bool:
        self.wd.implicitly_wait(0)
        delBtn = self.wd.find_elements(
            By.CSS_SELECTOR, '.result-list-item:first-child .result-list-item-btn-bar span:first-child')
        self.wd.implicitly_wait(10)
        if not delBtn:
            return False
        delBtn[0].click()
        self.wd.switch_to.alert.accept()
        return True

    def add_device_model(self, modelType, model, desc):
        select = Select(sampUi.wd.find_element(By.ID, 'device-type'))
        select.select_by_visible_text(modelType)
        ele = sampUi.wd.find_element(By.ID, 'device-model')
        ele.clear()
        ele.send_keys(model)
        description = sampUi.wd.find_element(By.ID, 'device-model-desc')
        description.clear()
        description.send_keys(desc)
        sampUi.wd.find_element(By.CSS_SELECTOR, '.add-one-submit-btn-div .btn').click()
        return

    def addSvcRule(self, ):
        # todo
        pass


sampUi = SMP_UI()
