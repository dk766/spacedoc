__author__ = "Valerian Chifu"
__email__ = "vchifu@gmail.com"
__version__ = "$Revision$"
__date__ = "$Date$"

from django.urls import path
from django.conf.urls import url
from spacedoc.docid.views import docdb_migrate_view, docid_generate_next_id_view, docid_get_templates_view, \
    docid_get_field_view, docid_get_field_values_by_docid_view, docid_register_id_view

urlpatterns = [
    url(r'^migrate/$', docdb_migrate_view, name='docid_migrate'),
    url(r'^generate-next-id/(\w.*)/$', docid_generate_next_id_view, name='docid_build_id'),
    url(r'^id/(\w.*)/$', docid_generate_next_id_view, name='docid_build_id'),
    url(r'^register-id/(\w.*)/$', docid_register_id_view, name='docid_build_id'),
    url(r'^templates/$', docid_get_templates_view, name='docid_templates'),
    url(r'^field/(\w.*)/$', docid_get_field_view, name='docid_templates'),
    url(r'^get-field/(\w.*)/$', docid_get_field_view, name='docid_templates'),
    url(r'^get-field-values/(\w.*)/$', docid_get_field_values_by_docid_view, name='docid_templates'),
]
