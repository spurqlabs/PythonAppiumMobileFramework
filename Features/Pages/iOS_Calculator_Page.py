import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


from Features.Pages.BasePage import Basepage


class iOS_Calculator_Page(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context

        self.add_operator = "//XCUIElementTypeStaticText[@name='+']"
        self.result = "(//XCUIElementTypeStaticText)[1]"

    def iOS_tap_number1(self,number):
        time.sleep(2)
        tap_on = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//XCUIElementTypeButton[@name='"+number+"']")))
        tap_on.click()

    def iOS_tap_operator(self):
        time.sleep(2)
        tap_on = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, self.add_operator)))
        tap_on.click()


    def iOS_equals(self, operator):
        time.sleep(2)
        tap_on = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, "//XCUIElementTypeStaticText[@name='"+operator+"']")))
        tap_on.click()


    def iOS_verify_result(self):
        sleep(5)
        try:
            verify_element = self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, self.result))).is_displayed()
        except NoSuchElementException:
            verify_element = False
        return verify_element


