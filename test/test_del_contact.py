# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    app.contact.delete_first_contact()
