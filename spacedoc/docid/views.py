
import re
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse

from spacedoc.docid.core.migrate.DocDBtoSpaceDoc import migrate
from spacedoc.docid.models import DocIdTemplate, DocIdTemplateField, RunningIds
from spacedoc.docid.core.misc import logger as log
from spacedoc.docid.core.misc import get_tags

def docdb_migrate_view(request):
    context ={}
    migrate()
    return HttpResponse('Migraton Done')


def docid_generate_next_id_view(request, template_id):
    context = {}

    log().info("Template Id: '%s'", template_id)
    template = DocIdTemplate.objects.get(id=template_id)
    field_names = get_tags(template.long_form, '<', '>')

    log().info("Field names: '%s'", field_names)

    return HttpResponse('Migraton Done')