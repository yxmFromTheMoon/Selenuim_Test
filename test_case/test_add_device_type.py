# 添加设备型号测试用例
import pytest
from selenium.webdriver.support.select import Select

from lib.webUI_smp import sampUi
from conftest import *
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def enterDeviceModelPage():
    sampUi.login('byhy', 'sdfsdf')
    # 有坑，记得sleep一下，否则无法跳到后续的url
    time.sleep(1)
    sampUi.wd.get(SMP_URL_ADD_MODEL_PAGE)
    print('****** 跳转添加型号页面 ******')
    yield


@pytest.fixture()
def delDeviceModel():
    yield
    print('****** 删除设备信号 ******')
    time.sleep(1)
    sampUi.delete_first_item()
    return


@pytest.mark.parametrize('select_type,model,description', [
    ('存储柜', '001', '001型号'),
    ('存储柜', '汉' * 100, '002型号')
])
def test_add_device_type(enterDeviceModelPage, delDeviceModel, select_type, model, description):
    addBtn = sampUi.wd.find_element(By.CSS_SELECTOR, '.add-one-area > span')
    if addBtn.text == '添加':
        addBtn.click()
    sampUi.add_device_model(select_type, model, description)
    deviceValues = sampUi.get_first_page_device_models()
    assert deviceValues == [[select_type, model, description]]
