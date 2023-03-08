from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import time
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help='username', type=str, required=False)
    parser.add_argument('--password', help='password', type=str, required=False)
    parser.add_argument('--ip', help='ip of the machine', type=str, required=False)
    parser.add_argument('--url', help='url to download the file for the dt', type=str, required=False)
    args = parser.parse_args()
    return args


arg = get_args()
username = arg.username
password = arg.password
ip = arg.ip
url = arg.url
srvc = Service("C:\\Users\\ariel\\Documents\\gecko\\geckodriver.exe")
driver = webdriver.Firefox(service=srvc)
driver.maximize_window()


def login():
    print("Trying to log in")
    driver.get("http://" + ip + "/login")
    driver.implicitly_wait(5)
    driver.find_element(by=By.NAME, value="username").send_keys(username)
    driver.find_element(by=By.NAME, value="password").send_keys(password)
    time.sleep(2)
    driver.find_element(by=By.TAG_NAME, value="button").click()
    print("Login success")


def create_dt():
    time.sleep(2)
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[1]/div/div[2]/header/div[1]/div/div[2]/div/div/div/span/button/span[1]").click()
    time.sleep(1)
    driver.find_element(by=By.NAME, value="name").send_keys("test")
    driver.find_element(by=By.NAME, value="version").send_keys("1")
    time.sleep(1)
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[3]/div[3]/div/form/div[2]/div/div[2]/button[2]/span[1]").click()
    time.sleep(1)
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[3]/div[3]/div/form/div[1]/div/div[2]/div[2]/div[1]/label/span["
                              "1]/span/input").click()

    driver.find_element(by=By.NAME, value="fileUrl").send_keys(url)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/form/div[2]/div/div[2]/button[3]").click()


def create_vul():
    time.sleep(10)
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[1]/div/nav/div/div/div[2]/div[1]/div/ul/div[3]/a/div[2]").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/nav/div/div/div[2]/div[1]/div/ul/div["
                                           "3]/div/div/div/ul/a[1]/div").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div[2]/div/button/span[1]").click()
    driver.find_element(by=By.NAME, value="name").send_keys("test")
    driver.find_element(by=By.ID, value="mui-component-select-type").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[3]/ul/li[1]").click()
    time.sleep(1)
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[3]/div[3]/div/form/div[2]/div/div[2]/button[2]/span[1]").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/form/div[1]/div[2]/div/div/div["
                                           "1]/div/div/div/div/div/button").send_keys(Keys.DOWN)
    driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/form/div[1]/div[2]/div/div/div["
                                           "1]/div/div/div/div/div/button").send_keys(Keys.ENTER)
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[3]/div[3]/div/form/div[2]/div/div[2]/button[3]/span[1]").click()


def create_zero():
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[1]/div/nav/div/div/div[2]/div[1]/div/ul/div[3]/a/div[2]").click()
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[1]/div/nav/div/div/div[2]/div[1]/div/ul/div[3]/div/div/div/ul/a[2]/div").click()
    time.sleep(10)
    driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div[2]/div/button/span[1]").click()
    driver.find_element(by=By.NAME, value="name").send_keys("test")
    driver.find_element(by=By.ID, value="mui-component-select-type").click()
    driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[3]/ul/li[2]").click()
    time.sleep(1)
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[3]/div[3]/div/form/div[2]/div/div[2]/button[2]/span[1]").click()

    driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/form/div[1]/div[2]/div/div/div["
                                           "1]/div/div/div/div/div/button").send_keys(Keys.DOWN)
    driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[3]/div/form/div[1]/div[2]/div/div/div["
                                           "1]/div/div/div/div/div/button").send_keys(Keys.ENTER)
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[3]/div[3]/div/form/div[2]/div/div[2]/button[3]/span[1]").click()



def main():
    get_args()
    login()
    create_dt()
    create_vul()
    create_zero()
    print('success')


if __name__ == '__main__':
    main()
