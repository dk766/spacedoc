__author__ = "Valerian Chifu"
__email__ = "vchifu@gmail.com"
__copyright__ = ""
__version__ = "$"
__date__ = "$"

from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)