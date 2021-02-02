from selenium.webdriver.common.by import By


class AddCustomers:
    link_customers_menu_xpath = (By.XPATH, "(//span[text()='Customers'])[1]")
    link_customers_xpath = (By.XPATH, "(//span[text()='Customers'])[2]")
    button_add_customer_xpath = (By.XPATH, "//*[@href='/Admin/Customer/Create']")
    text_enter_email_id = (By.ID, "Email")
    text_enter_password_id = (By.ID, "Password")
    text_enter_first_name_id = (By.ID, "FirstName")
    text_enter_last_name_id = (By.ID, "LastName")
    radio_btn_female_id = (By.ID, "Gender_Female")
    radio_btn_male_id = (By.ID, "Gender_Male")
    text_enter_dob_id = (By.ID, "DateOfBirth")
    text_enter_company_id = (By.ID, "Company")
    list_newsletter_id = (By.ID, "SelectedNewsletterSubscriptionStoreIds_taglist")
    list_store_link_text = (By.LINK_TEXT, "Test store 2")
    list_customer_roles_id = (By.ID, "SelectedCustomerRoleIds_taglist")
    list_administrator_link_text = (By.LINK_TEXT, "Administrators")
    dropdown_vendor_id = (By.ID, "VendorId")
    checkbox_active_id = (By.ID, "Active")
    textarea_admin_comment_id = (By.ID, "AdminComment")
    button_save_css = (By.CSS_SELECTOR, "button[name='save']")
    button_save_continue_css = (By.CSS_SELECTOR, "button[name='save-continue']")

    def __init__(self, driver):
        self.driver = driver

    def click_customers_menu(self):
        self.driver.find_element(*AddCustomers.link_customers_menu_xpath).click()

    def click_customers(self):
        self.driver.find_element(*AddCustomers.link_customers_xpath).click()

    def add_customer(self):
        self.driver.find_element(
            By.XPATH, *AddCustomers.button_add_customer_xpath
        ).click()

    def enter_email_id(self, email):
        self.driver.find_element(By.ID, *AddCustomers.text_enter_email_id).clear()
        self.driver.find_element(By.ID, *AddCustomers.text_enter_email_id).send_keys(
            email
        )

    def enter_password(self, password):
        self.driver.find_element(By.ID, *AddCustomers.text_enter_password_id).clear()
        self.driver.find_element(By.ID, *AddCustomers.text_enter_password_id).send_keys(
            password
        )

    def enter_first_name(self, fname):
        self.driver.find_element(By.ID, *AddCustomers.text_enter_first_name_id).clear()
        self.driver.find_element(
            By.ID, *AddCustomers.text_enter_first_name_id
        ).send_keys(fname)

    def enter_last_name(self, lname):
        self.driver.find_element(By.ID, *AddCustomers.text_enter_last_name_id).clear()
        self.driver.find_element(
            By.ID, *AddCustomers.text_enter_last_name_id
        ).send_keys(lname)

    def select_gender(self, gender):
        if gender in ("Male", "male"):
            self.driver.find_element(By.ID, *AddCustomers.radio_btn_male_id).click()
        elif gender in ("Female", "female"):
            self.driver.find_element(By.ID, *AddCustomers.radio_btn_female_id).click()

    def enter_birth_date(self, birth_date):
        self.driver.find_element(By.ID, *AddCustomers.text_enter_dob_id).clear()
        self.driver.find_element(By.ID, *AddCustomers.text_enter_dob_id).send_keys(
            birth_date
        )

    
