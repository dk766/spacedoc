
import re
import json
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse

from spacedoc.docid.core.migrate.DocDBtoSpaceDoc import migrate
from spacedoc.docid.core.docid_utils import docid_generate_next_id, docid_get_templates, docid_get_field_info, \
    docid_get_field_values_by_docid, docid_register_id


def docid_generate_next_id_view(request, template_id):
    context = {''}
    params = {'originator': 'INSTITUTION', 'project_element': 'BRANCH', 'doc_type': 'MOM', 'issue': 3, 'revision': 5}
    (docid_long, docid_short) = docid_generate_next_id(template_id, params)

    return HttpResponse("DocID:  '{}' DocID (ShortForm): '{}'".format(docid_long, docid_short))


def docid_register_id_view(request, template_id):
    context = {''}
    params = {'originator': 'INSTITUTION', 'project_element': 'BRANCH', 'doc_type': 'MOM',
              'issue': 3, 'revision': 5, 'number': '0006'}
    (docid_long, docid_short) = docid_register_id(params, template_id=template_id)

    return HttpResponse("DocID:  '{}' DocID (ShortForm): '{}'".format(docid_long, docid_short))


def docid_get_templates_view(request):
    json_str = docid_get_templates()
    return HttpResponse("{}".format(json_str))


def docid_get_field_view(request, field_name):
    json_str = json.dumps(docid_get_field_info(field_name))
    return HttpResponse("{}".format(json_str))


def docid_get_field_values_by_docid_view(request, docid):
    params = docid_get_field_values_by_docid(docid)
    return HttpResponse(json.dumps(params))