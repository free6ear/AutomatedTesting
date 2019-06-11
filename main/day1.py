from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import unittest


class SCSAutomatedTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get('http://192.168.40.44:8086/hwe/ui/epm/epmportal.html?appId=5')

    def test_EPM(self):
        driver = self.driver
        driver.execute_script('document.body.style.zoom="1.25"')

        driver.find_element_by_name('username').send_keys('pbsadmin')
        driver.find_element_by_name('password').send_keys('1qaz2wsx')

        sleep(5)

        login_button = driver.find_element_by_id('loginbtn')
        driver.execute_script('arguments[0].click()', login_button)

        sleep(10)

        driver.find_element_by_xpath('//*[@id="isc_37"]/table/tbody/tr/td').click()

        sleep(10)

        target = driver.find_element_by_xpath('//*[@id="isc_9Etable"]/tbody/tr[45]/td/div/table/tbody/tr/td[3]')
        for i in range(3):
            driver.execute_script('arguments[0].click()', target)
        sleep(20)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    '''
        verbosity = 0(静默模式):仅仅获取总的测试用例数及总的结果
        verbosity = 1(默认模式):此时在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
        verbosity = 2(详细模式):测试结果会显示每个测试用例的所有相关信息
    '''
    unittest.main(verbosity=2)
