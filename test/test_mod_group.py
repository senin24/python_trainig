# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="python_test_group2", header="python_test_group_Logo2", footer="python_test_group_Comment2"))
    app.session.logout()