# 登录测试用例
import time
import pytest
from selenium.webdriver.common.by import By

from lib.webUI_smp import sampUi


def test_login_001(clearAlert):
    sampUi.login('byhy', 'sdfsdf')
    nav = sampUi.wd.find_element(By.TAG_NAME, 'nav')
    assert nav != []

@pytest.mark.parametrize('username,password, expectalert', [
    (None, 'sdfsdf', '请输入用户名'),
    ('byhy', None, '请输入密码'),
    ('byhy', 'sdfsdfs', '登录失败： 用户名或者密码错误'),
    ('byhy', 'sdfsd', '登录失败： 用户名或者密码错误'),
    ('byhyb', 'sdfsdf', '登录失败： 用户名不存在'),
    ('byh', 'sdfsdf', '登录失败： 用户名不存在')
])
def test_login_002(username, password, expectalert, clearAlert):
    sampUi.login(username, password)
    time.sleep(1)
    alert = sampUi.wd.switch_to.alert
    assert alert.text == expectalert

@pytest.fixture()
def clearAlert():
    yield
    try:
        sampUi.wd.switch_to.alert.accept()
    except Exception as e:
        print(e)