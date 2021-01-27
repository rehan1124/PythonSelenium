from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class PythonHomePage:
    """
    PythonHomePage class will hold page objects for website: https://www.python.org/
    Locators are defined as class variables so that it is flexible to modify at one
    place and then later re-use it anywhere
    """

    search_field = (By.ID, "id-search-field")

    def __init__(self, driver):
        """
        Create driver to be used with other instance methods
        :param driver:
        :type driver:
        """
        self.driver = driver

    def enter_text_in_search(self, text):
        """
        Enter the text for which search is to be done
        :param text:
        :type text:
        :return:
        :rtype:
        """
        element = self.driver.find_element(*PythonHomePage.search_field)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)
        return element
