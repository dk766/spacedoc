__author__ = "Valerian Chifu"
__email__ = "vchifu@gmail.com"
__version__ = "$Revision$"
__date__ = "$Date$"

from django.urls import path
from django.conf.urls import url
from spacedoc.docid.views import docdb_migrate_view, docid_generate_next_id_view

urlpatterns = [
    url(r'^migrate/$', docdb_migrate_view, name='docid_migrate'),
    url(r'^generate_next_id/$', docid_generate_next_id_view, name='docid_build_id'),
    url(r'^id/(\w.*)/$', docid_generate_next_id_view, name='docid_build_id'),
]