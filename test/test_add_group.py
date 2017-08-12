# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="python_test_group", header="python_test_group_Logo", footer="python_test_group_Comment"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login( username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()