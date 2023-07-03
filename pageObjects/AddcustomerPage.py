import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.customLogger import LogGen
import pytest

class AddCustomer:
    # Add customer Page
    logger = LogGen.loggen()  # Logger
    lnkCustomers_menu_xpath = "//html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    lnkCustomers_menuitem_xpath = "//html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    btnAddnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[1]/div[2]/input"
    txtPassword_xpath = "//html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[2]/div[2]/div/input"
    txtcustomerRoles_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitemAdministrators_xpath = "/html/body/div[6]/div/div[2]/ul/li[1]"
    lstitemRegistered_xpath = "/html/body/div[6]/div/div[2]/ul/li[4]"
    lstitemGuests_xpath = "/html/body/div[6]/div/div[2]/ul/li[3]"
    lstitemVendors_xpath = "/html/body/div[6]/div/div[2]/ul/li[5]"
    drpmgrOfVendor_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[11]/div[2]/select"
    rdMaleGender_id = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[5]/div[2]/div/div[1]/label"
    rdFeMaleGender_id = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[5]/div[2]/div/div[2]/label"
    txtFirstName_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[3]/div[2]/input"
    txtLastName_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[4]/div[2]/input"
    txtDob_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[6]/div[2]/span[1]/span/input"
    txtCompanyName_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[7]/div[2]/input"
    txtAdminContent_xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[13]/div[2]/textarea"
    btnSave_xpath = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()
        self.logger.info("************* CLICK OM MENU **********")

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuitem_xpath).click()
        self.logger.info("************* CLICK OM CUSTOMER **********")

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()
        self.logger.info("************* CLICK OM ADD **********")

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)
        self.logger.info("************* SET EMAIL **********")

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)
        self.logger.info("************* SET PASSWORD **********")

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem =  self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem =  self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"/html/body/div[6]/div/div[2]/ul/li[3]").click()
            self.listitem =  self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem =  self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem =  self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem =  self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)
        self.logger.info("************* SET ROLES **********")

    def setManagerOfVendor(self, value):
        drp =self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath)
        drp1=Select(drp)
        self.logger.info("************* SET VENDOR **********")

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGender_id).click()
        self.logger.info("************* SET GENDER **********")

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)
        self.logger.info("************* SET FIRST NAME **********")

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)
        self.logger.info("************* SET LAST NAME **********")

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)
        self.logger.info("************* SET DOB **********")

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)
        self.logger.info("************* SET company NAME **********")

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)
        self.logger.info("************* SET admin comment **********")

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()
        self.logger.info("************* CLICK SAVE **********")
