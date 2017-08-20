# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Senin2", lastname="Pavel2", email="psenin@mail.ru2", bday="23",
                               bmonth="May", byear="1990"))