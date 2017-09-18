# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    # old_contacts = app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    # assert len(old_contacts) + 1 == app.contact.count()
    # new_contacts = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    print(sorted(old_contacts, key=Contact.id_or_max))
    print(sorted(new_contacts, key=Contact.id_or_max))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        db_list = map(app.contact.clean, new_contacts)
        ui_list = map (app.contact.clean, app.contact.get_contact_list())

        assert sorted(db_list, key=Contact.id_or_max) == sorted(ui_list, key=Contact.id_or_max)