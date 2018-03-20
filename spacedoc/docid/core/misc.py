__author__ = "Valerian Chifu"
__email__ = "vchifu@gmail.com"
__version__ = "$"
__date__ = "$"

import re
import logging
import inspect


def configure_default(level=logging.WARNING):
    logging.basicConfig(level=level,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M')

    a_handler = logging.StreamHandler()
    a_handler.setLevel(level)
    a_formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    a_handler.setFormatter(a_formatter)


def logger(object=None):
    name_prefix = '' if object is None else '{}.'.format(object.__class__.__name__)
    full_name = name_prefix+inspect.currentframe().f_back.f_code.co_name
    return logging.getLogger(full_name)


def get_tags(s, open_delim ='<', close_delim ='>' ):
    return re.findall(r'{}(.+?){}'.format(open_delim, close_delim), s)

