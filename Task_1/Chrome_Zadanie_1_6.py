import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class Tele2_tasks(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_tele2(self):
        driver = self.driver
        driver.get(" https://more.tele2.ru")

        pictures = driver.find_element_by_class_name(
            'main-content'
        ).find_elements_by_tag_name('img')
        for i in pictures:
            link = i.get_attribute('src')
            print(link)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
