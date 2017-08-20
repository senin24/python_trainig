class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_link_text("add new").click()
        for attr, value in contact.__dict__.items():
            if (str(attr) == 'bday') or (str(attr) == 'bmonth'):
                wd.find_element_by_xpath(
                    "//select[@name='" + value.xpath + "']/*[@value='" + value.value + "']").click()
                continue
            wd.find_element_by_name(value.xpath).send_keys(value.value)
        wd.find_element_by_name("submit").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath(".//*[@title='Edit']").click()
        self.create(contact)
