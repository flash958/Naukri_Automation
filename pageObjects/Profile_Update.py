from selenium.webdriver.common.by import By

class ProfileUpdate:

    btn_viewprofile = "//div[@class='view-profile-wrapper']"
    btn_editprofile = "//em[@class='icon edit']"
    btn_saveprofile = "//button[@id='saveBasicDetailsBtn']"

    def __init__(self,driver):
        self.driver=driver

    def clickViewProfile(self):
        self.driver.find_element(By.XPATH,self.btn_viewprofile).click()

    def clickEditProfile(self):
        self.driver.find_element(By.XPATH,self.btn_editprofile).click()

    def clickSavePProfile(self):
        self.driver.find_element(By.XPATH,self.btn_saveprofile).click()

