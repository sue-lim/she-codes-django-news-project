# handlers.py
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.template import loader

def custom_permission_denied(request, exception):
    template = loader.get_template('custom_permission_denied.html')
    return HttpResponseForbidden(template.render({}, request))
