__author__ = "Valerian Chifu"
__email__ = "vchifu@gmail.com"
__version__ = "$"
__date__ = "$"


import logging
from spacedoc.docid.core.misc import configure_default
from spacedoc.docid.core.misc import logger as log
from spacedoc.docweb.models import DocumentEntity, DocumentStatus


def migrate():

    documents = DocumentEntity.objects.using('default').all()

    log().info("There are %s documents in the database", len(documents))
    for document in documents:
        log().info("Doc: '%s'", document)


def main():
    # configure the logging

    migrate()

if __name__ == '__main__':
    main()
