from selenium import webdriver
from selenium.webdriver.common.by import By

class NaukriHomePage:

    # Locators Data
    btn_login_id="login_Layer"
    email_text_xpath="//input[@class='err-border']"
    password_text_xpath="//input[@placeholder='Enter your password']"
    popup_switch="//div[@class='drawer-wrapper ']"
    submit_btn="//button[@class='btn-primary loginButton']"

    # Functions to access the Home Page Information

    def __init__(self,driver):
        self.driver=driver


    def setemail(self,email):
        self.driver.find_element(By.XPATH,self.popup_switch).click()
        self.driver.find_element(By.XPATH,self.email_text_xpath).send_keys(email)

    def setpassword(self, pwd):

        self.driver.find_element(By.XPATH,self.password_text_xpath).send_keys(pwd)

    def click_login_btn(self):
        self.driver.find_element(By.ID,self.btn_login_id).click()
        print("Successfully clicked")


    def final_login(self):
        self.driver.find_element(By.XPATH,self.submit_btn).click()


