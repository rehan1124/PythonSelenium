from selenium.webdriver.common.by import By


class Login:
    textbox_username_id = (By.ID, "Email")
    textbox_password_id = (By.ID, "Password")
    button_login_css = (By.CSS_SELECTOR, "input[value='Log in']")
    link_logout_linktext = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*Login.textbox_username_id).clear()
        self.driver.find_element(*Login.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*Login.textbox_password_id).clear()
        self.driver.find_element(*Login.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(*Login.button_login_css).click()
