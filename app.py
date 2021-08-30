import requests
from subprocess import check_output
from time import sleep

from sel_start import init_driver

from plyer import notification

BROWSER_DRIVER_PATH = ""
BROWSER_EXECUTABLE_PATH = ""

WIFI_SSID = ""
WIFI_LOGIN_URL = ""
WIFI_USERNAME = ""
WIFI_PASSWORD = ""

USERNAME_ELEMENT_ID = "username"
PASSWORD_ELEMENT_ID = "password"
LOGIN_ELEMENT_ID = "loginbutton"


def is_connected():
    try:

        requests.get("https://google.com")
        return True
    except:
        return False


def login(url: str, username: str, password: str):
    driver = init_driver(headless=True)

    driver.get(url)
    sleep(2)
    username_element = driver.find_element_by_id(USERNAME_ELEMENT_ID)
    password_element = driver.find_element_by_id(PASSWORD_ELEMENT_ID)
    username_element.clear()
    password_element.clear()
    username_element.send_keys(username)
    password_element.send_keys(password)
    driver.find_element_by_id(LOGIN_ELEMENT_ID).click()
    sleep(2)
    driver.quit()


if __name__ == "__main__":
    if WIFI_SSID in check_output("netsh wlan show interfaces").decode(
            'utf-8') and not is_connected():
        login(url=WIFI_LOGIN_URL,
              username=WIFI_USERNAME,
              password=WIFI_PASSWORD)
        notification.notify(title="WiFi Connected!",
                            message="Connected to WiFi using script.",
                            app_name="Auto WiFi Login")
