# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from contact import Contact
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

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

    def open_home_page(self):
        wd = self.wd
        wd.get("http://192.168.10.214/addressbook/index.php")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath(".//*[@id='LoginForm']/input[@value='Login']").click()

    def open_contacts_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        success = True
        wd = self.wd
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="Senin", lastname="Pavel", email="psenin@mail.ru", bday="24",
                                        bmonth="December", byear="1981"))
        self.logout()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
