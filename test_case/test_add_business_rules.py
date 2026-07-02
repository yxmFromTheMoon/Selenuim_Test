# 添加业务规则测试用例
import pytest

from lib.webUI_smp import sampUi
from conftest import *
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def enterRulePage():
    sampUi.login('byhy', 'sdfsdf')
    # 有坑，记得sleep一下，否则无法跳到后续的url
    time.sleep(1)
    sampUi.wd.get(SMP_URL_RULES)
    print('****** 跳转添加规则页面 ******')
    yield


@pytest.fixture()
def delRule():
    yield
    print('****** 删除规则 ******')
    time.sleep(1)
    sampUi.delete_first_item()
    return


def test_add_device_type(enterRulePage, delRule):
    addBtn = sampUi.wd.find_element(By.CSS_SELECTOR, '.add-one-area > span')
    if addBtn.text == '添加':
        addBtn.click()
    sampUi.addSvcRule()
    # TODO
    pass
