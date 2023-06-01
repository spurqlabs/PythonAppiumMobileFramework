from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time

from Features.Pages.BasePage import Basepage


class android_Calculator_Page(Basepage):
    def __init__(self, context):
        Basepage.__init__(self, context.driver)
        self.context = context

        self.number1 = "(//android.widget.Button)[5]"
        self.add = "//android.widget.Button[@content-desc='plus']"
        self.number2 = "(//android.widget.Button)[9]"
        self.operator_equals = "(//android.widget.Button)[13]"
        self.verify = "(//android.widget.TextView)[2]"

    def tap_number1(self):
        time.sleep(2)
        tap_on = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, self.number1)))
        tap_on.click()

    def tap_operator(self):
        time.sleep(2)
        tap_on = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, self.add)))
        tap_on.click()

    def tap_number2(self):
        time.sleep(2)
        tap_on = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, self.number2)))
        tap_on.click()

    def equals(self):
        time.sleep(2)
        tap_on = self.wait.until(
            EC.presence_of_element_located((MobileBy.XPATH, self.operator_equals)))
        tap_on.click()

    def verify_result(self):
        try:
            verify_element = self.wait.until(EC.presence_of_element_located(
                (MobileBy.XPATH, self.verify))).is_displayed()
        except NoSuchElementException:
            verify_element = False

        return verify_element



