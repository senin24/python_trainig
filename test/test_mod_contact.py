# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Pavel_test_modify_random_contact"))
    # old_contacts = app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    contact_for_modify = random.choice(old_contacts)
    contact = Contact(firstname="Senin2_test_modify_random_contact", lastname="Pavel2", email="psenin@mail.ru2", bday="23",
            bmonth="May", byear="1990")
    app.contact.modify_contact_by_id_bd(contact, contact_for_modify.id)
    # assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[old_contacts.index(contact_for_modify)]=new_contacts[old_contacts.index(contact_for_modify)]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        db_list = map(app.contact.clean, new_contacts)
        ui_list = map(app.contact.clean, app.contact.get_contact_list())

        assert sorted(db_list, key=Contact.id_or_max) == sorted(ui_list, key=Contact.id_or_max)