from selenium.webdriver.common.by import By
from Utilities.Config_Reader import Read_Locators

class Login_page():
    # TextBox_username_ID="Email"
    # TextBox_password_ID="Password"
    # Login_Button_XPATH='//button[contains(text(),"Log in")]'
    # Logout_Button_Xpath="//a[contains(text(),'Logout')]"
    
    TextBox_username_ID=Read_Locators.get_TextBox_username_ID()
    TextBox_password_ID=Read_Locators.get_TextBox_password_ID()
    Login_Button_XPATH=Read_Locators.get_Login_Button_XPATH()
    Logout_Button_Xpath=Read_Locators.get_Logout_Button_Xpath()
    
    
    def __init__(self,driver):
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element(By.ID,self.TextBox_username_ID).clear()
        self.driver.find_element(By.ID,self.TextBox_username_ID).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.ID,self.TextBox_password_ID).clear()
        self.driver.find_element(By.ID,self.TextBox_password_ID).send_keys(password)
    
    def Login_Click(self):
        self.driver.find_element(By.XPATH,self.Login_Button_XPATH).click()

    def Logout_Click(self):
        self.driver.find_element(By.XPATH,self.Logout_Button_Xpath).click()