import inspect
from page_objects.login_page import Login
from utilities.read_config import *
from utilities.custom_logger import LogGen


@pytest.mark.usefixtures("create_driver")
class TestLoginPage:
    log = LogGen.log_gen()
    cfg = get_config()
    USERNAME = cfg["E-COMMERCE"]["ADMIN_EMAIL"]
    PASSWORD = cfg["E-COMMERCE"]["ADMIN_PASSWORD"]

    def test_home_page_title(self):
        login_page_title = self.driver.title
        self.log.info("***** test_home_page_title ****")
        self.log.info(f"Login page title: {login_page_title}")
        assert login_page_title == "Your store. Login", self.driver.save_screenshot(
            "./Screenshots/" + inspect.stack()[0][3]
        )
        self.log.info("Title successfully verified. Closing the browser now.")

    def test_login_page_title(self):
        login_driver = Login(self.driver)
        self.log.info("***** test_login_page_title ****")
        login_driver.enter_username(self.USERNAME)
        self.log.info(f"Entered Username: {self.USERNAME}")
        login_driver.enter_password(self.PASSWORD)
        self.log.info(f"Entered Password: {self.PASSWORD}")
        login_driver.click_login()
        assert (
            self.driver.title == r"Dashboard / nopCommerce administration"
        ), self.driver.save_screenshot("./Screenshots/" + inspect.stack()[0][3])
        self.log.info("Login is successful.")
        self.log.info("Closing the browser now.")
