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

        self.driver.get('http://192.168.40.42:8086/hwe/ui/epm/epmportal.html?appId=5')

    def test_EPM(self):
        driver = self.driver

        driver.find_element_by_name('username').send_keys('pbsadmin')
        driver.find_element_by_name('password').send_keys('1qaz2wsx')

        loginbtn = WebDriverWait(self.driver, 10)\
            .until(expected_conditions.element_to_be_clickable((By.ID, 'loginbtn')))
        loginbtn.click()

        manage_templete_btn = WebDriverWait(self.driver, 10)\
            .until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="isc_37"]/table/tbody/tr/td')))
        manage_templete_btn.click()


        add_templete_btn = WebDriverWait(self.driver, 10)\
            .until(expected_conditions.element_to_be_clickable((By.NAME, 'isc_8Fmain')))
        add_templete_btn.click()

        sleep(1)

        display_name =  driver.find_element_by_name('isc_TextItem_2')
        display_name.send_keys('Haier_Simulation_Analysis')

        sleep(1)

        category = driver.find_element_by_name('isc_ComboBoxItem_0')
        category.send_keys('Haier')

        sleep(1)

        description = driver.find_element_by_name('isc_TextAreaItem_0')
        description.send_keys('test')

        sleep(1)

        driver.find_element_by_name('isc_C5main').click()
        driver.find_element_by_name('fileUploader').send_keys(r'D:\work\templete\Process\Haier_simulation_analysis_process\processArtifacts\HaierAnalysis.zip')

        sleep(5)

        upload_btn = WebDriverWait(self.driver, 10)\
            .until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Cancel')))
        upload_btn.click()

        sleep(3)

        driver.find_element_by_name('isc_DLmain').click()

        sleep(3)

        driver.find_element_by_xpath('//*[@id="isc_A1table"]/tbody/tr[1]/td[1]/div/nobr/img')
        driver.find_element_by_xpath('//*[@id="isc_AJtable"]/tbody/tr[1]/td[1]/div/nobr/img')
        driver.find_element_by_xpath('//*[@id="isc_AX"]/table/tbody/tr/td')

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
