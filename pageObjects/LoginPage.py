from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login_selector="body > div.master-wrapper-page > div > div > div > div > div.page-body > div.customer-blocks > div > form > div.buttons > button"
    link_logout_linktest="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR,self.button_login_selector).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktest).click()