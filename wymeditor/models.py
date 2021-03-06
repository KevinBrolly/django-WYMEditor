from django.db import models
from django.contrib.admin import widgets as admin_widgets

from widgets import WYMEditorWidget, AdminWYMEditor
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^wymeditor\.models\.WYMEditorField'])
except ImportError:
    pass


class WYMEditorField(models.TextField):

    def formfield(self, **kwargs):
        defaults = {'widget': WYMEditorWidget}
        defaults.update(kwargs)

        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = AdminWYMEditor

        return super(WYMEditorField, self).formfield(**defaults)
