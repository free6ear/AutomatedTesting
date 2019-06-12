from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest
from time import sleep


class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        #设置隐式等待时间30s
        self.driver.implicitly_wait(30)

        self.driver.maximize_window()

        self.driver.get('http://demo.magentocommerce.com')

    def test_register_new_user(self):
        driver = self.driver

        driver.find_element_by_link_text("My Account").click()
        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div/div[2]/div/button')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        first_name = driver.find_element_by_id('firstname')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        country = driver.find_element_by_id('country')

        first_name.send_keys('Test')
        last_name.send_keys('User1')
        email_address.send_keys('TestUser_150214_2200@example.com')

        #下拉选择
        selector = Select(driver.find_element_by_name('country'))
        selector.select_by_value('CN')

        selector = Select(driver.find_element_by_name('company_type'))
        selector.select_by_value('development')

        selector = Select(driver.find_element_by_name('individual_role'))
        selector.select_by_value('technical/developer')

        password = driver.find_element_by_name('password')
        confirm_password = driver.find_element_by_name('confirmation')

        password.send_keys('Nc4b8shi4')
        confirm_password.send_keys('Nc4b8shi4')

        #勾选同意协议
        driver.find_element_by_id('agree_terms').click()

        driver.find_element_by_id('registerSubmit').click()


if __name__ == '__main__':
    unittest.main(verbosity=2)





