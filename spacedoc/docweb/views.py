from django.shortcuts import render
from django.views.generic.base import TemplateView
from django_tables2 import RequestConfig
from .tables import DocsTable
from .models import DocumentEntity


class BlankView(TemplateView):
    template_name = 'docweb/page.html'


def home_view(request):
    # To decide if a homepage is necessary
    return render(request, 'docweb/page.html',{})


def wip_view(request):
    # To decide if a homepage is necessary
    return render(request, 'docweb/wip.html',{})


def search_view(request):
    context = {}
    return docs_view(request)
    # return render(request, 'docweb/search.html', context)


def docs_view(request):
    context ={}
    db_entries = DocumentEntity.objects.all()
    table = DocsTable(db_entries)
    context['total_docs_num'] = len(db_entries)
    RequestConfig(request, paginate=False).configure(table)
    # table.paginate(page=request.GET.get('page', 1), per_page=500)
    context['docs'] = table

    return render(request, 'docweb/docs.html', context)