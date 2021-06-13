from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://github.com/")
search = driver.find_element_by_name('q')
search.send_keys("selenium python")
search.send_keys(Keys.RETURN)
tag = driver.find_elements_by_class_name("topic-tag")
tag = [i.text for i in tag]
assert 'python' in tag and 'webdriver' in tag and 'selenium' in tag
star = driver.find_element_by_css_selector(".starring-container > a").click()
title = driver.find_element_by_css_selector('h1')
assert title.text == 'Sign in to GitHub'
username = driver.find_element_by_name('login')
username.send_keys('username')
password = driver.find_element_by_name('password')
password.send_keys('qwerty123')
password.send_keys(Keys.RETURN)
error = driver.find_element_by_xpath('//*[@id="login"]/p')
assert error.text == 'There have been several failed attempts to sign in ' \
                     'from this account or IP address. Please wait a while and try again later.'
driver.close()