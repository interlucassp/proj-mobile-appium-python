import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

@pytest.fixture
def driver():
    caps = {
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:app": "/caminho/para/Android-NativeDemoApp.apk",  # atualize com o seu
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    yield driver
    driver.quit()

def test_login_sucesso(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login").click()
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "input-email").send_keys("teste@email.com")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "input-password").send_keys("123456")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "button-LOGIN").click()
    mensagem = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Welcome").text
    assert "Welcome" in mensagem
