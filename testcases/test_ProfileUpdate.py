import time
from selenium.webdriver.common.by import By
from pageObjects.Naukri_Home_Page import NaukriHomePage
from pageObjects.Profile_Update import ProfileUpdate



class Test_ProfileUpd:
    baseURL = "https://www.naukri.com/"

    def test_profileupdation(self,setup):

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Navigation to HomePage
        self.hp=NaukriHomePage(self.driver)
        self.hp.click_login_btn()
        time.sleep(5)
        #self.driver.find_element(By.XPATH,"//div[@class='drawer-wrapper ']").click()
        self.hp.setemail("saxena958@gmail.com")
        self.hp.setpassword("Sunshine@312")
        self.hp.final_login()

        # Profile Updation
        self.up=ProfileUpdate(self.driver)
        time.sleep(5)
        self.up.clickViewProfile()
        time.sleep(5)
        self.up.clickEditProfile()
        time.sleep(5)
        ele=self.driver.find_element(By.XPATH,self.up.btn_saveprofile)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ele)
        time.sleep(5)
        self.up.clickSavePProfile()

        





