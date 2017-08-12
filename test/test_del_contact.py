# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()
