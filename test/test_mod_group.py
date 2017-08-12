# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="python_test_group", header="python_test_group_Logo", footer="python_test_group_Comment"))
    app.session.logout()