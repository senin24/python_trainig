from collections import namedtuple
from sys import maxsize

t_contact = namedtuple("Field", ["value", "xpath"])


class Contact:
    def __init__(self, id=None, firstname=None, lastname=None, nickname=None, company=None, title=None, address=None,
                 home=None, mobile=None, work=None, phone2=None, email=None, email2=None, email3=None, homepage=None,
                 bday=None, bmonth=None, byear=None, all_emails_from_home_page=None, all_phones_from_home_page=None):
        self.id = t_contact(id, "id")
        self.firstname = t_contact(firstname, "firstname")
        self.lastname = t_contact(lastname, "lastname")
        self.nickname = t_contact(nickname, "nickname")
        self.company = t_contact(company, "company")
        self.title = t_contact(title, "title")
        self.address = t_contact(address, "address")
        self.home = t_contact(home, "home")
        self.mobile = t_contact(mobile, "mobile")
        self.work = t_contact(work, "work")
        self.phone2 = t_contact(phone2, "phone2")
        self.email = t_contact(email, "email")
        self.email2 = t_contact(email2, "email2")
        self.email3 = t_contact(email3, "email3")
        self.homepage = t_contact(homepage, "homepage")
        self.bday = t_contact(bday, "bday")
        self.bmonth = t_contact(bmonth, "bmonth")
        self.byear = t_contact(byear, "byear")
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "id - %s | firstname - %s | lastname - %s" % (self.id.value, self.firstname.value, self.lastname.value)

    def __eq__(self, other):
        return ((self.id.value is None) or (other.id.value is None) or (self.id.value == other.id.value)) \
               and (self.firstname.value == other.firstname.value) and (self.lastname.value == other.lastname.value)

    def id_or_max(self):
        if self.id.value:
            return int(self.id.value)
        else:
            return maxsize
