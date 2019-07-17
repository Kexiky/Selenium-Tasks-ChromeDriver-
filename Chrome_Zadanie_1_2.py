import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://msk.tele2.ru")

        tariffs = driver.find_element_by_class_name(
            'ssc-tariffs-container'
        ).find_elements_by_class_name('swiper-slide')
        for i in range(len(tariffs)):
            try:
                tariffs[i].find_element_by_class_name('hit-image')
                flag = True
            except NoSuchElementException:
                flag = False
            name_tariff = tariffs[i].find_element_by_class_name('tariff-title').text
            if flag:
                print('Тариф ' + name_tariff + ' - ХИТ продаж')
            else:
                print('Тариф ' + name_tariff + ' - не ХИТ продаж')
            driver.find_element_by_class_name("swiper-arrow-next").click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()