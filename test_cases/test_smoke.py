from utilities.read_config import *
from page_objects.python_home_page import *
import time


class TestSmoke(Utils):
    def test_python_home_page(self):
        """
        Test for making search in Python homepage and confirming results are found.
        :return:
        :rtype:
        """
        php = PythonHomePage(self.driver)
        utl = Utils()
        php.enter_text_in_search(text="pycon")
        utl.assert_content_absence("No results found.", self.driver.page_source)
        time.sleep(10)
