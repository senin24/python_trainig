from collections import namedtuple

t_contact = namedtuple("Field", ["value", "xpath"])


class Contact:
    def __init__(self, firstname="", lastname="", nickname="", company="", title="", address="", home="", mobile="",
                 email="", homepage="", bday="", bmonth="", byear=""):
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
