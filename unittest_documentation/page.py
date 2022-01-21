class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title_matching(self):
        if "Python" in self.driver.title:
            return True
    
    def click_go_button(self):
        element = self.driver.find_element()
        element.click()