from django.shortcuts import render
from django.views.generic.base import TemplateView
from .tables import DocsTable
from .models import DocumentEntity


class BlankView(TemplateView):
    template_name = 'spacedocweb/page.html'


def docs_view(request):
    context ={}
    db_entries = DocumentEntity.objects.all()
    table = DocsTable(db_entries)
    context['total_docs_num'] = len(db_entries)
    table.paginate(page=request.GET.get('page', 1), per_page=50)
    context['docs'] = table

    return render(request, 'spacedocweb/docs.html', context)