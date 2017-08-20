# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="python_test_group", header="python_test_group_Logo", footer="python_test_group_Comment"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))