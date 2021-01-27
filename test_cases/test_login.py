import inspect
from page_objects.login_page import Login
from utilities.read_config import *


@pytest.mark.usefixtures("create_driver")
class TestLoginPage:
    cfg = get_config()
    BASE_URL = cfg["E-COMMERCE"]["ADMIN_URL"]
    USERNAME = cfg["E-COMMERCE"]["ADMIN_EMAIL"]
    PASSWORD = cfg["E-COMMERCE"]["ADMIN_PASSWORD"]
    EXECUTABLE_PATH = "browser_driver/chromedriver.exe"

    def test_home_page_title(self):
        login_page_title = self.driver.title
        print(f"Login page title: {login_page_title}")
        assert login_page_title == "Your store. Login", self.driver.save_screenshot(
            "./Screenshots/" + inspect.stack()[0][3]
        )
        print("Title successfully verified. Closing the browser now.")

    def test_login_page_title(self):
        login_driver = Login(self.driver)
        login_driver.enter_username(self.USERNAME)
        print(f"Entered Username: {self.USERNAME}")
        login_driver.enter_password(self.PASSWORD)
        print(f"Entered Password: {self.PASSWORD}")
        login_driver.click_login()
        assert (
            self.driver.title == r"Dashboard / nopCommerce administration"
        ), self.driver.save_screenshot("./Screenshots/" + inspect.stack()[0][3])
        print("Login is successful.")
        print("Closing the browser now.")
