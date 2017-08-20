# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Senin", lastname="Pavel", email="psenin@mail.ru", bday="24",
                               bmonth="December", byear="1981"))