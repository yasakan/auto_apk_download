import unittest
from appium import webdriver
import os
import time


class AppiumSampleTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.android.vending'
        desired_caps['appActivity'] = 'com.google.android.finsky.activities.MainActivity'
        desired_caps['automationName'] = 'Appium'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
        # self.driver.set_script_timeout(6)

    def tearDown(self):
        self.driver.quit()

    def test(self):
        element = self.driver.find_element_by_id("com.android.vending:id/search_box_idle_text")
        element.click()
        self.driver.find_element_by_id("com.android.vending:id/search_box_text_input").send_keys("google")
        self.driver.press_keycode(66)
        time.sleep(5)
        # self.driver.find_element_by_link_text("インストール").click()
        elements = self.driver.find_elements_by_xpath("//android.widget.Button")
        # elements.pop(0).click()
        print(len(elements))
        for element in elements:
            if element.text == "インストール":
                element.click()
        time.sleep(60)
        os.system('adb devices')


if __name__ == '__main':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumSampleTest)
    unittest.TextTestRunner().run(suite)
