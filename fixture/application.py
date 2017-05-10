from selenium import webdriver
from os import environ
from selenium.webdriver.remote.remote_connection import RemoteConnection
from sauceclient import SauceClient

class Application:
    def __init__(self, browser_config, test_name):
        self.browser_config = browser_config
        self.test_name = test_name
        username = environ.get('SAUCE_USERNAME', 'vp962888')
        access_key = environ.get('SAUCE_ACCESS_KEY', 'a05d42a4-efe7-4cbd-80b2-04e7e85025e4')
        selenium_endpoint = "https://%s:%s@ondemand.saucelabs.com:443/wd/hub" % (username, access_key)
        self.sauce_client = SauceClient(username, access_key)
        build_tag = environ.get('BUILD_TAG', None)
        tunnel_id = environ.get('TUNNEL_IDENTIFIER', None)
        desired_cap = dict()
        desired_cap.update(self.browser_config)
        desired_cap['build'] = build_tag
        desired_cap['tunnelIdentifier'] = tunnel_id
        executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
        desired_cap['name'] = self.test_name
        self.wd = webdriver.Remote(command_executor=executor, desired_capabilities=desired_cap)
        self.wd.implicitly_wait(60)

    def submit_request_consultation_form(self):
        wd = self.wd
        wd.find_element_by_name("send").click()
        assert len(wd.find_elements_by_xpath("//div[@id='wrapper']//h1[.='Thank you']")) > 0
        self.sauce_client.jobs.update_job(wd.session_id, passed=True)

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