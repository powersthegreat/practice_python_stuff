import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.python.org")

    def test_example_1(self):
        assert True

    def test_example_2(self):
        assert True
    
    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matching()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()