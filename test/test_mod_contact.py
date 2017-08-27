# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Pavel"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Senin2", lastname="Pavel2", email="psenin@mail.ru2", bday="23",
            bmonth="May", byear="1990")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    print(old_contacts)
    print(new_contacts)
    old_contacts[0]=contact
    print(sorted(old_contacts, key=Contact.id_or_max))
    print(sorted(new_contacts, key=Contact.id_or_max))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)