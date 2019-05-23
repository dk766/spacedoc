from collections import OrderedDict

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.http.response import HttpResponse
from django_tables2 import RequestConfig

from spacedoc.docid.core.misc import logger as log
from spacedoc.docid.core.docid_utils import docid_get_templates, docid_get_field_info


from .tables import DocsTable
from .models import DocumentEntity


class BlankView(TemplateView):
    template_name = 'docweb/page.html'


def home_view(request):
    # To decide if a homepage is necessary
    return render(request, 'docweb/page.html',{})


def wip_view(request):
    # To decide if a homepage is necessary
    db_entities = DocumentEntity.objects.all()
    text = ''
    for entity in db_entities:
        docid = entity.docid
        elems = docid.split('-')
        elems.pop(0)
        last = elems.pop(-1)
        tmp = last.split('_')
        elems.append(str(int(tmp.pop(0))))
        version = tmp.pop(0)[1:]
        elems = elems + version.split('.')
        log().info("Elements are: %s", elems)
        formatted_text = '{' + '}{'.join(elems) + '}'
        log().info("Formatted text is : %s", formatted_text)
        text = '{}<br><code>{}</code>'.format(text, formatted_text)
        entity.docfields = formatted_text
        entity.save()

    return HttpResponse(text)


def register_view(request):
    context = {}
    log().info("Register document")
    templates_list = docid_get_templates()
    # for now I only use first template TODO fix this
    template = templates_list[0]
    context['docid_template'] = template['long_form']
    context['fields'] = template['fields']
    params = OrderedDict()
    for field_str in template['fields']:
        # context[field_str] = docid_get_field_info(field_str)['values']
        model_dict = docid_get_field_info(field_str)
        params[field_str] = model_dict

    context['params'] = params
    log().error("Params:'%s'", params)

    return render(request, 'docweb/register_doc.html', context)


def search_str_view(request, param_str):
    log().info("Searching '%s'", param_str)
    # TODO implement
    return docs_view(request)


def search_view(request):
    context = {}
    # return docs_view(request)
    if (request.method == 'POST') and ('cmd' in request.POST):
        cmd = request.POST['cmd']
        log().debug('You try to execute "{}" Good luck with that !'.format(cmd))
    else:
        cmd = ''
        log().debug('Since no command was requested will use default')

    if cmd == 'Search':
        param_str = request.POST.get('search-str', '%')
        if len(param_str) == 0:
            param_str = '%'
        log().debug("Search string is '%s'", param_str)
        result = redirect(reverse('spacedoc_search_str', args=[param_str]))
    else:
        result = render(request, 'docweb/search.html', context)

    # return HttpResponse("Search page ...")
    return result


def docs_view(request):
    context = {}
    db_entries = DocumentEntity.objects.all()
    table = DocsTable(db_entries)
    context['total_docs_num'] = len(db_entries)
    RequestConfig(request, paginate=False).configure(table)
    # table.paginate(page=request.GET.get('page', 1), per_page=500)
    context['docs'] = table

    return render(request, 'docweb/docs.html', context)
