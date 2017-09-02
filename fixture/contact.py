from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (
            wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath("//input[@value='Delete']")) > 0):
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
            if str(attr) == "id" or (str(attr) == 'all_address_from_home_page') or (
                str(attr) == 'all_emails_from_home_page') or (
                        str(attr) == 'all_phones_from_home_page'):
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

    def delete_contact_by_id(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_id(0)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_xpath(".//*[@title='Edit']")[index].click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_xpath(".//*[@title='Details']")[index].click()

    def modify_contact_by_id(self, contact, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contacts_cache = None

    def modify_first_contact(self, contact, index):
        self.modify_contact_by_id(contact, 0)

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
                address = wd.find_element_by_xpath(table_xpath + "[" + str(i + 1) + "]/td[4]").text
                all_emails = wd.find_element_by_xpath(table_xpath + "[" + str(i + 1) + "]/td[5]").text
                all_phones = wd.find_element_by_xpath(table_xpath + "[" + str(i + 1) + "]/td[6]").text
                self.contacts_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                   address=address, all_emails_from_home_page=all_emails,
                                                   all_phones_from_home_page=all_phones))
                i = i + 1
        return list(self.contacts_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        contact_for_attr = Contact()
        tmp = []
        for attr, value in contact_for_attr.__dict__.items():
            if (str(attr) == 'all_address_from_home_page') or (str(attr) == 'all_emails_from_home_page') or (
                str(attr) == 'all_phones_from_home_page'):
                continue
            tmp.append(wd.find_element_by_name(value.xpath).get_attribute("value"))
        return Contact(id=tmp[0], firstname=tmp[1], lastname=tmp[2], nickname=tmp[3], company=tmp[4], title=tmp[5],
                       address=tmp[6], home=tmp[7], mobile=tmp[8], work=tmp[9], phone2=tmp[10], email=tmp[11],
                       email2=tmp[12], email3=tmp[13], homepage=tmp[14], bday=tmp[15], bmonth=tmp[16], byear=tmp[17])
