from selenium import webdriver
from Test_Cases.conftest import Setup
from Page_Object.Login_Page import Login_page
from Utilities.Config_Reader import Read_Config

class Test_01_login():
    # url="https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # username="admin@yourstore.com"
    # password="admin"
    url=Read_Config.get_url()
    username=Read_Config.get_username()
    password=Read_Config.get_password()


    def test_homepage_title(self,Setup):
        self.driver=Setup
        self.driver.get(self.url)
        actual_title=self.driver.title
        if actual_title=="nopCommerce demo store. Login":
            assert True
        else:
            assert False
            self.driver.save_screenshot(".//Screenshots/test_homepage_title.png")
        self.driver.quit()

    def test_login(self,Setup):
        self.driver=Setup
        self.driver.get(self.url)
        Login=Login_page(self.driver)
        Login.set_username(self.username)
        Login.set_password(self.password)
        Login.Login_Click()
        

        actual_title=self.driver.title

        if actual_title=="Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
            self.driver.save_screenshot(".//Screenshots/test_login.png")
        
        Login.Logout_Click()
        self.driver.quit()

        
    