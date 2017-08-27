# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Pavel"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Senin2", lastname="Pavel2", email="psenin@mail.ru2", bday="23",
            bmonth="May", byear="1990")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index]=contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)