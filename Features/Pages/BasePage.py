from selenium.webdriver.support.ui import WebDriverWait


# In the base page we are creating an object of driver.
# We are using this driver in the other pages and environment page.

class Basepage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.implicit_wait = 25

