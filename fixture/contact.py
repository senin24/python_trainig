from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath("//input[@value='Delete']")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.contacts_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        for attr, value in contact.__dict__.items():
            if str(attr) == "id":
                continue
            if value.value is None:
                continue
            if (str(attr) == 'bday') or (str(attr) == 'bmonth'):
                wd.find_element_by_xpath(
                    "//select[@name='" + value.xpath + "']/*[@value='" + value.value + "']").click()
                continue
            wd.find_element_by_name(value.xpath).click()
            wd.find_element_by_name(value.xpath).clear()
            wd.find_element_by_name(value.xpath).send_keys(value.value)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath(".//*[@title='Edit']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contacts_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contacts_cache = []
            table_xpath = "//*[@id='maintable']//tr[@name]"
            i = 0
            while i < len(wd.find_elements_by_xpath(table_xpath)):
                id = wd.find_element_by_xpath(table_xpath + "[" + str(i + 1) + "]/td[1]/input").get_attribute("id")
                firstname = wd.find_element_by_xpath(table_xpath + "[" + str(i + 1) + "]/td[3]").text
                lastname = wd.find_element_by_xpath(table_xpath + "[" + str(i + 1) + "]/td[2]").text
                self.contacts_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
                i = i + 1
        return list(self.contacts_cache)



