from element_infos.main_page import MainPage
from element_infos.login_page import LoginPage
class QuitBase:
    def __init__(self,driver):
        self.mainpage = MainPage(driver)

    def quit(self):
        self.mainpage.user_info_click()
        self.mainpage.quit_login_click()
        return LoginPage(self.mainpage.driver)