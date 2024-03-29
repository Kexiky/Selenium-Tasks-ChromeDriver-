import unittest
from selenium import webdriver

class Tele2_tasks(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_tele2(self):
        driver = self.driver
        driver.get("https://msk.tele2.ru")
        tariffs = driver.find_element_by_class_name(
            'ssc-tariffs-container'
        ).find_elements_by_class_name('swiper-slide')

        print("Жирный шрифт:")
        for i in tariffs:
            fatfont = i.find_elements_by_tag_name('strong')
            for j in fatfont:
                print(j.text)
                driver.find_element_by_class_name("swiper-arrow-next").click()





    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()