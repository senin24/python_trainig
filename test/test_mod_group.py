# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_random_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # old_groups = app.group.get_group_list()
    old_groups = db.get_group_list()
    # index = randrange(len(old_groups))
    group_for_modify = random.choice(old_groups)
    group = Group(name="New group for test_modify_random_group_name")
    app.group.modify_group_by_id(group, group_for_modify.id)
    # assert len(old_groups) == app.group.count()
    # new_groups = app.group.get_group_list()

    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)

    old_groups[old_groups.index(group_for_modify)] = new_groups[old_groups.index(group_for_modify)]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        db_list = map(clean, new_groups)
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_modify_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_first_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="New footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)