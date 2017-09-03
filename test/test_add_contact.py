# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "_" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#TODO create: random names, emails, telephones, www addreses

testdata = [Contact(firstname="", lastname="", nickname="", company="", title="", address="",
                 home="", mobile="", work="", phone2="", email="", email2="", email3="", homepage="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            company=random_string("company", 20), title=random_string("title", 10), address=random_string("address", 40),
            home=random_string("home", 10), mobile=random_string("mobile", 10), work=random_string("work", 10),
            phone2=random_string("phone2", 10), email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email3", 20), homepage=random_string("homepage", 10)
            )
    for i in range(5)
]
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    # contact = Contact(firstname="Senin", lastname="Pavel", email="psenin@mail.ru", bday="24",
    #                            bmonth="December", byear="1981")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    print(sorted(old_contacts, key=Contact.id_or_max))
    print(sorted(new_contacts, key=Contact.id_or_max))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)