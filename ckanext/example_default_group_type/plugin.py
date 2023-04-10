from __future__ import annotations
from collections.abc import Iterable
import os
from typing import Any, Optional

import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan.lib.plugins import DefaultGroupForm, DefaultTranslation


class ExampleDefaultGroupTypePlugin(
    p.SingletonPlugin, DefaultGroupForm, DefaultTranslation
):
    p.implements(p.IGroupForm, inherit=True)
    p.implements(p.ITemplateHelpers)
    p.implements(p.ITranslation)

    def is_fallback(self) -> bool:
        return True

    def group_types(self) -> Iterable[str]:
        return ["category"]

    def get_helpers(self):
        return {
            "humanize_entity_type": humanize_entity_type,
        }



@tk.chained_helper
def humanize_entity_type(
    next_: Any, entity_type: str, object_type: str, purpose: str
) -> Optional[str]:
    templates = {
        "add link": tk._("Add category"),
        "breadcrumb": tk._("Categories"),
        "content tab": tk._("Categories"),
        "create label": tk._("Create category"),
        "create title": tk._("Create category"),
        "delete confirmation": tk._(
            "Are you sure you want to delete this category?"
        ),
        "description placeholder": tk._(
            "A little information about my category..."
        ),
        "edit label": tk._("Edit category"),
        "facet label": tk._("Categories"),
        "form label": tk._("Category Form"),
        "main nav": tk._("Categories"),
        "my label": tk._("My categories"),
        "view label": tk._("View category"),
        "name placeholder": tk._("My category"),
        "no any objects": tk._(
            "There are currently no categories for this site"
        ),
        "no associated label": tk._(
            "There are no categories associated with this dataset"
        ),
        "no description": tk._("There is no description for this category"),
        "no label": tk._("No category"),
        "page title": tk._("Categories"),
        "save label": tk._("Save category"),
        "search placeholder": tk._("Search categories..."),
        "you not member": tk._("You are not a member of any categories."),
        "update label": tk._("Update category"),
    }

    if object_type == "category" and purpose in templates:
        return templates[purpose]

    return next_(entity_type, object_type, purpose)
