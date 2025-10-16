import configparser

class Read_Config:
    config=configparser.RawConfigParser()
    config.read(".//Configarations\config.ini")

    @classmethod
    def get_url(cls):
        return cls.config.get("Details","Url")
    
    @classmethod
    def get_username(cls):
        return cls.config.get("Details","username")
    
    @classmethod
    def get_password(cls):
        return cls.config.get("Details","password")
    
class Read_Locators:
    config=configparser.RawConfigParser()
    config.read(".//Configarations\Locator.ini")

    @classmethod
    def get_TextBox_username_ID(cls):
        return cls.config.get("Login","TextBox_username_ID")
    
    @classmethod
    def get_TextBox_password_ID(cls):
        return cls.config.get("Login","TextBox_password_ID")
    
    @classmethod
    def get_Login_Button_XPATH(cls):
        return cls.config.get("Login","Login_Button_XPATH")
    
    @classmethod
    def get_Logout_Button_Xpath(cls):
        return cls.config.get("Login","Logout_Button_Xpath")
    