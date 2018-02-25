__author__ = "Valerian Chifu"
__email__ = "vchifu@gmail.com"
__version__ = "$"
__date__ = "$"

import django_tables2 as tables
from .models import DocumentEntity


class DocsTable(tables.Table):

    class Meta:
        model = DocumentEntity
        attrs = {'class': 'table table-striped table-bordered table-hover'}
    # name = tables.LinkColumn('docgen_download', args=[A('task_id')])
