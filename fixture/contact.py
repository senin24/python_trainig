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
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        for attr, value in contact.__dict__.items():
            if value.value is None:
                continue
            if (str(attr) == 'bday') or (str(attr) == 'bmonth'):
                wd.find_element_by_xpath(
                    "//select[@name='" + value.xpath + "']/*[@value='" + value.value + "']").click()
                continue
            wd.find_element_by_name(value.xpath).send_keys(value.value)

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
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))
