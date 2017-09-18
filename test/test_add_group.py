# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    # old_groups = app.group.get_group_list()
    old_groups = db.get_group_list()
    # group = Group(name="python_test_group", header="python_test_group_Logo", footer="python_test_group_Comment")
    app.group.create(group)
    # assert len(old_groups) + 1 == app.group.count()
    # new_groups = app.group.get_group_list()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        db_list = map(app.group.clean, new_groups)
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)