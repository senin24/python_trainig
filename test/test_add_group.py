# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="python_test_group", header="python_test_group_Logo", footer="python_test_group_Comment"))
    app.logout()


def test_add_empty_group(app):
    app.login( username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()