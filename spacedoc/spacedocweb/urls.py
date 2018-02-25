__author__ = "Valerian Chifu"
__email__ = "vchifu@gmail.com"
__version__ = "$Revision$"
__date__ = "$Date$"

from django.conf.urls import url
from spacedoc.spacedocweb.views import BlankView, docs_view
    # , HomeView

urlpatterns = [
    # url(r'^home/$', HomeView.as_view(), name='spacedoc_home'),
    url(r'^blank/$', BlankView.as_view(), name='spacedoc_blank'),
    url(r'^docs/$', docs_view, name='spacedoc_docs'),
    # url(r'^login/$', login_view, name='spacedoc_login'),
    # url(r'^logout/$', logout_view, name='spacedoc_logout'),

]