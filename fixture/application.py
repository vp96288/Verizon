from selenium.webdriver.firefox.webdriver import WebDriver


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)


    def submit_request_consultation_form(self):
        wd = self.wd
        wd.find_element_by_name("send").click()
        wd.find_element_by_xpath("//div[@id='wrapper']//h1[.='Thank you']").click()

    def change_field_value(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_consultation_form2(self, personal_info):
        wd = self.wd
        self.change_field_value("fname", personal_info.firstname)
        self.change_field_value("lname", personal_info.lastname)
        self.change_field_value("email", personal_info.email)
        self.change_field_value("phone", personal_info.phone)
        self.change_field_value("company", personal_info.company)
        if not wd.find_element_by_xpath("//select[@id='_db_ad_state']//option[6]").is_selected():
            wd.find_element_by_xpath("//select[@id='_db_ad_state']//option[6]").click()
        self.change_field_value("zip", personal_info.zipcode)

    def fill_request_consultation_form1(self):
        wd = self.wd
        if not wd.find_element_by_xpath("//select[@id='_db_country']//option[2]").is_selected():
            wd.find_element_by_xpath("//select[@id='_db_country']//option[2]").click()
        if not wd.find_element_by_xpath("//div[@class='step1']/label[2]/select//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@class='step1']/label[2]/select//option[2]").click()
        if not wd.find_element_by_xpath("//select[@class='topic']//option[17]").is_selected():
            wd.find_element_by_xpath("//select[@class='topic']//option[17]").click()
        if not wd.find_element_by_xpath("//select[@id='_db_industry']//option[20]").is_selected():
            wd.find_element_by_xpath("//select[@id='_db_industry']//option[20]").click()
        wd.find_element_by_link_text("Next step").click()

    def open_request_consultation(self):
        wd = self.wd
        if not wd.find_element_by_xpath("//select[@id='phonecountry']//option[34]").is_selected():
            wd.find_element_by_xpath("//select[@id='phonecountry']//option[34]").click()
        wd.find_element_by_xpath("//div[@class='contactsales']//a[.='Contact Us']").click()

    def open_how_we_can_help_you(self):
        wd = self.wd
        wd.find_element_by_link_text("Contact Us").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://www.verizonenterprise.com/")

    def destroy(self):
        self.wd.quit()