import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProprties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_login:
    baseUrl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremailL()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("********************Test-001-Login************")
        self.logger.info("********************Verifying Home Page Title**************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.logger.error("********************Home Page Title Test Is Passed**************")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********************Home Page Title Test Is Failed**************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********************Verifying Login Test**************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.error("********************Login Test Is Passed**************")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********************Login Test Is Failed**************")
            assert False
