from sys import maxsize


class Contact:
    def __init__(self, id=None, firstname=None, lastname=None, nickname=None, company=None, title=None, address=None,
                 home=None, mobile=None, work=None, phone2=None, email=None, email2=None, email3=None, homepage=None,
                 bday=None, bmonth=None, byear=None, all_emails_from_home_page=None, all_phones_from_home_page=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.title = title
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "id - %s | firstname - %s | lastname - %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return ((self.id is None) or (other.id is None) or (self.id == other.id)) \
               and (self.firstname == other.firstname) and (self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
