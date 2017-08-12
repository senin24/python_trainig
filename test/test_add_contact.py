# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Senin", lastname="Pavel", email="psenin@mail.ru", bday="24",
                               bmonth="December", byear="1981"))
    app.session.logout()