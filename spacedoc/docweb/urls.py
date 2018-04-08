__author__ = "Valerian Chifu"
__email__ = "vchifu@gmail.com"
__version__ = "$Revision$"
__date__ = "$Date$"

from django.conf.urls import url
from spacedoc.docweb.views import BlankView, docs_view, home_view, search_view, search_str_view, register_view, \
    wip_view


urlpatterns = [
    url(r'^home/$', home_view, name='spacedoc_home'),
    url(r'^blank/$', BlankView.as_view(), name='spacedoc_blank'),
    url(r'^docs/$', docs_view, name='spacedoc_docs'),
    url(r'^search/$', search_view, name='spacedoc_search'),
    url(r'^search/(\w.*)$', search_str_view, name='spacedoc_search_str'),
    url(r'^register/$', register_view, name='spacedoc_register_doc'),
    # url(r'^login/$', login_view, name='spacedoc_login'),
    # url(r'^logout/$', logout_view, name='spacedoc_logout'),

    url(r'^wip/$', wip_view, name='spacedoc_wip'),
]

