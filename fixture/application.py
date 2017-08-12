from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper (self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://192.168.10.214/addressbook/index.php")

    def open_contacts_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, contact):
        wd = self.wd
        self.open_contacts_page()
        for attr, value in contact.__dict__.items():
            if (str(attr) == 'bday') or (str(attr) == 'bmonth'):
                wd.find_element_by_xpath(
                    "//select[@name='" + value.xpath + "']/*[@value='" + value.value + "']").click()
                continue
            wd.find_element_by_name(value.xpath).send_keys(value.value)
        wd.find_element_by_name("submit").click()

    def destroy(self):
        self.wd.quit()