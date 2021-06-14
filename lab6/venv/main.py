from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time


class GitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://github.com/")

    def test_01(self):
        # check for existing Google title in page google.com
        assert "Git" in self.driver.page_source

    def test_02(self):
        #to find input field and print selenium python
        search = self.driver.find_element_by_name('q')
        search.send_keys("selenium python")
        search.send_keys(Keys.RETURN)

        #get tags from result of search and compare with python, webdriver, selenium
        tag = self.driver.find_elements_by_class_name("topic-tag")
        tag = [i.text for i in tag]
        assert 'python' in tag and 'webdriver' in tag and 'selenium' in tag
        star = self.driver.find_element_by_css_selector(".starring-container > a").click()

        #singin git
        title = self.driver.find_element_by_css_selector('h1')
        assert title.text == 'Sign in to GitHub'

        #find username field and fill it
        username = self.driver.find_element_by_name('login')
        username.send_keys('new_login')

        #find password field and fill it
        password = self.driver.find_element_by_name('password')
        password.send_keys('qwerty123')
        password.send_keys(Keys.RETURN)
        error = self.driver.find_element_by_xpath('//*[@id="login"]/p')
        assert error.text == 'There have been several failed attempts to sign in ' \
                             'from this account or IP address. Please wait a while and try again later.'

    def tearDown(self) -> None:
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()