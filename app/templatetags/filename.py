import os
from django import template

register = template.Library()

@register.filter
def filename(value):
    return os.path.basename(value.file.name)

@register.filter
def filesize(value):
    """Returns the filesize of the filename given in value"""
    return os.path.getsize(value)