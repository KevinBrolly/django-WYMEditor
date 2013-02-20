from django import forms
from django.contrib.admin import widgets as admin_widgets
from django.conf import settings
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode


class WYMEditorWidget(forms.Textarea):

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        attrs['class'] = attrs.get('class', '') + ' wymeditor'
        final_attrs = self.build_attrs(attrs, name=name)
        
        wym_config = getattr(settings, 'WYMEDITOR_CONFIG', '')
        
        html = u'<textarea%s>%s</textarea>' % (flatatt(final_attrs),
                conditional_escape(force_unicode(value)))

        html += u'<script type="text/javascript">\
                jQuery(function() {\
                    if(window.wymeditor==undefined){\
                        jQuery(".wymeditor").wymeditor(%s);\
                        window.wymeditor=true\
                    }\
                });</script>' % wym_config
        return mark_safe(html)

    class Media:
        js = ("wymeditor/jquery/jquery.js",
              "wymeditor/jquery.wymeditor.min.js",)


class AdminWYMEditor(admin_widgets.AdminTextareaWidget, WYMEditorWidget):
    pass
