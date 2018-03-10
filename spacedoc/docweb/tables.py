__author__ = "Valerian Chifu"
__email__ = "vchifu@gmail.com"
__version__ = "$"
__date__ = "$"

import django_tables2 as tables
import logging
from .models import DocumentEntity


class DocsTable(tables.Table):
    docid = tables.Column(verbose_name='Doc ID', attrs={'td': {'style': 'width:40%'}})
    status = tables.Column(verbose_name='Status', attrs={'td': {'style': 'width:10%'}})
    owner = tables.Column(verbose_name='Owner', attrs={'td': {'style': 'width:5%'}})
    group = tables.Column(verbose_name='Group', attrs={'td': {'style': 'width:10%'}})
    author = tables.Column(verbose_name='Author', attrs={'td': {'style': 'width:10%'}})
    title = tables.Column(verbose_name='Title', attrs={'td': {'style': 'width:10%'}})

    creation_date = tables.DateColumn(verbose_name='Creation Date',attrs={'td': {'style': 'width:10%'}})
    submission_date = tables.DateColumn(verbose_name='Submission Date',attrs={'td': {'style': 'width:10%'}})
    doc_date = tables.DateColumn(verbose_name='Document Date', attrs={'td': {'style': 'width:10%'}})
    creation_date = tables.Column(verbose_name='Creation Date', attrs={'td': {'style': 'width:10%'}})
    files = tables.Column(verbose_name='Files', attrs={'td': {'style': 'width:10%'}})


    def render_files(self, value, column, record):
        pdf = record['doc']
        logging.getLogger(self).info("pdf='%s'", pdf)
        new_value = " \n".join([pdf])
        print("werwerew", pdf, new_value)
        return new_value

    class Meta:
        model = DocumentEntity
        attrs = {'class': 'table table-striped table-bordered table-hover', 'id': 'datatable'}
        exclude = ('id', 'creation_date', 'submission_date', 'stop_date', 'doc_date', 'creation_date', 'doc', 'zip')
        orderable = False
