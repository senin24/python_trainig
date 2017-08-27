from collections import namedtuple
from sys import maxsize

t_contact = namedtuple("Field", ["value", "xpath"])


class Contact:
    def __init__(self, firstname=None, lastname=None, nickname=None, company=None, title=None, address=None, home=None, mobile=None,
                 email=None, homepage=None, bday=None, bmonth=None, byear=None, id=None):
        self.id = t_contact(id, "id")
        self.firstname = t_contact(firstname, "firstname")
        self.lastname = t_contact(lastname, "lastname")
        self.nickname = t_contact(nickname, "nickname")
        self.company = t_contact(company, "company")
        self.title = t_contact(title, "title")
        self.address = t_contact(address, "address")
        self.home = t_contact(home, "home")
        self.mobile = t_contact(mobile, "mobile")
        self.email = t_contact(email, "email")
        self.homepage = t_contact(homepage, "homepage")
        self.bday = t_contact(bday, "bday")
        self.bmonth = t_contact(bmonth, "bmonth")
        self.byear = t_contact(byear, "byear")

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