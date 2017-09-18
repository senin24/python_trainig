# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import time


def test_delete_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Pavel_test_delete_random_contact"))
    # old_contacts =  app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id_bd(contact.id)

    # assert len(old_contacts) - 1 == app.contact.count()
    time.sleep(1)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        db_list = map(app.contact.clean, new_contacts)
        ui_list = map (app.contact.clean, app.contact.get_contact_list())

        assert sorted(db_list, key=Contact.id_or_max) == sorted(ui_list, key=Contact.id_or_max)
