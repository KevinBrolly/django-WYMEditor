django-WYMEditor
================

This application will allow you to use [WYMEditor](http://http://www.wymeditor.org/) on your django TextFields.

Inspired by django-tinymce - https://github.com/aljosa/django-tinymce

Usage
-----

Add the application to your INSTALLED_APPS:

    INSTALLED_APPS = (
        ...
        'wymeditor',
    )

The easiest way to use the widget is to use the WYMEditorField in your model:

    from django.db import models
    from wymeditor.models import WYMEditorField

    class MyModel(models.Model):
        html_content = WYMEditorField()

To customize the editor you can use the WYMEDITOR_CONFIG setting:

    WYMEDITOR_CONFIG = {
        'classesItems': [
            {'name': 'example_class', 'title': 'Example Class', 'expr': 'p'}
        ],
    }

License
-------

This program is licensed under the MIT License.

WYMEditor is dual licensed under [MIT](http://opensource.org/licenses/mit-license.php) and [GPL](http://www.gnu.org/copyleft/gpl.html) licenses.
