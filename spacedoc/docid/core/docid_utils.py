__author__ = "Valerian Chifu"
__email__ = "vchifu@gmail.com"
__version__ = "$"
__date__ = "$"

import json

from spacedoc.docid.models import DocIdTemplate, DocIdTemplateField, DocIdTemplateTypes, TypeRunningId, \
    TypeConstant, TypeMap, TypeSequence, TypeTree, DocIdFieldValue
from spacedoc.docid.core.misc import logger as log
from spacedoc.docid.core.misc import get_tags


TAG_START = '<'
TAG_END = '>'


def docid_generate_next_id(template_id, params):
    """
    Builds the long and short form of the docid for the template with the provided id using the values from the
    provided parameters dictionary
    :param template_id: the id of an template
    :param params: a dictionary with parameters and their values
    :return: a tuple (long_id, short_id)
    """
    db_template = DocIdTemplate.objects.get(id=template_id)
    check_params(db_template, params)
    # field_names = get_tags(db_template.long_form, '<', '>')
    # log().info("Field names: %s", field_names)
    running_numbers_fields = get_running_number_fields(db_template)
    for field_str in running_numbers_fields:
        next_id = get_next_running_number(db_template, field_str, params)
        params[field_str] = next_id

    (long_id, short_id) = docid_register_id(params, db_template=db_template)

    return (long_id, short_id)


def docid_register_id(params, template_id=None, db_template=None):
    """
    Builds the long and short form of the docid for the template with the provided id using the values from the
    provided parameters dictionary
    :param template_id: the id of an template
    :param params: a dictionary with parameters and their values
    :return: a tuple (long_id, short_id)
    """
    if db_template is None and (template_id is not None):
        db_template = DocIdTemplate.objects.get(id=template_id)

    long_id = build_id(db_template.long_form, params)
    short_id = build_id(db_template.short_form, params)

    # Check if docid is already registered and if yes throws and ValueError
    db_objects = DocIdFieldValue.objects.filter(docid=long_id)
    if len(db_objects) :
        raise ValueError("The docid '{}' is already registered".format(long_id))

    # Save the field values
    for field_str in get_tags(db_template.long_form, TAG_START, TAG_END):
        field_value = DocIdFieldValue(docid=long_id, field_id=get_field_by_field_name(field_str),
                                      template_id=db_template, value=params[field_str])
        field_value.save()

    return (long_id, short_id)


def check_params(template_model, params):
    """
    Checks if the provided parameters are correct (name and value) according to the provided template model
    :param template_model: the template model
    :param params: a dict containing as keys the field names and as value their values. The running_id fields are
    ignored in this checking
    :return: true for success or throws an ValueError for the frst error encountered
    """
    #TODO: implement
    return True


def build_id(template_str, params):
    """
    Builds an id based on the provided template (as a string 'template_str') and the 'params' dict
    :param template_str: the docid template string
    :param params: the parameters dictionary
    :return: the docid corresponding to the provided params or throws ValueError
    """
    if template_str is None:
        raise ValueError('The template cannot be None')

    field_names = get_tags(template_str, TAG_START, TAG_END)
    for field_str in field_names:
        if field_str in params:
            value = params[field_str]
        else:
            value = ''
        log().info("template '%s' current field: '%s'", template_str, field_str)
        template_str = template_str.replace('{}{}{}'.format(TAG_START, field_str, TAG_END), str(value))

    return template_str


def get_running_number_fields(template_model):
    """
    Returns the names of all the the fields of type DocIdTemplateTypes.RUNNING_ID for the provided template
    :param template_model:
    :return: a list of field names of type DocIdTemplateTypes.RUNNING_ID
    """
    fields = []
    field_names = get_tags(template_model.long_form, TAG_START, TAG_END)
    for field_name in field_names:
        dbfield = DocIdTemplateField.objects.get(field_name=field_name)
        if dbfield.field_type == DocIdTemplateTypes.RUNNING_ID:
            fields.append(field_name)

    return fields


def get_next_running_number(template_model, field_name, params):
    """
    Generates the next available number for the provided field_name in the provided template_model and with the provided
    parameters. The new number is also saved in the DB
    :param template_model: a template model
    :param field_name: the field nime of type DocIdTemplateTypes.RUNNING_ID
    :param params: a dict with parameters (necessary for the field_name)
    :return: the newly generated number as a string (with the required formatting)
    """
    dbfieldname = DocIdTemplateField.objects.get(field_name=field_name)
    db_ob = TypeRunningId.objects.get(field_name=dbfieldname)
    fieldnames = get_tags(db_ob.fields_list, TAG_START, TAG_END)
    fields_value = ''
    docid_list = None
    for field_str in fieldnames:
        if field_str in params:
            kwargs = {
                'field_id':  get_field_by_field_name(field_str),
                'value':  params[field_str],
            }
            if docid_list is None:
                docid_list = DocIdFieldValue.objects.filter(template_id=template_model).filter(**kwargs).values_list('docid', flat=True)
                log().debug("1. fieldstr='%s' fieldvalue='%s' docid_list=%s",field_str,params[field_str], docid_list)
            else:
                docid_list = DocIdFieldValue.objects.filter(docid__in=docid_list).filter(**kwargs).values_list('docid', flat=True)
                log().debug("2. fieldstr='%s' fieldvalue='%s' docid_list=%s",field_str,params[field_str], docid_list)
        else:
            raise ValueError("Parameter '{}' is missing. A new running_id cannot be built for '{}'".format(
                field_str, field_name
            ))

    if len(docid_list):
        db_field = DocIdFieldValue.objects.filter(docid__in=docid_list).filter(field_id=get_field_by_field_name(field_name)).order_by('-value')

        for ob in db_field:
            log().debug("Value='%s'", ob.value)
        running_num = int(db_field[0].value) + 1
    else:
        running_num = 1

    # Formatting of the generated number
    new_value_str = str(running_num)
    while len(new_value_str) < db_ob.digits_number:
        new_value_str = "0{}".format(new_value_str)
    log().info("fields_value='%s'", fields_value)

    return new_value_str


def docid_get_templates():
    """
    Returns the templates as json format
    :return: a list of json objects
    """
    template_models = DocIdTemplate.objects.all()
    templates_list = []
    for template_model in template_models:
        templates_list.append(template_model.to_json())
    return templates_list


def get_field_by_field_name(field_name):
    return DocIdTemplateField.objects.get(field_name=field_name)


def docid_get_field_info(field_name):
    log().debug("Loading Field with name '%s'", field_name)
    field_model = DocIdTemplateField.objects.get(field_name=field_name)
    fields_dict = field_model.to_dict()
    log().debug("Dict representation of this object is: '%s'", fields_dict)
    fields_dict['values'] = []
    if field_model.field_type == DocIdTemplateTypes.CONSTANT:
        fieldtype_models = TypeConstant.objects.filter(field_name=field_model)
    elif field_model.field_type == DocIdTemplateTypes.RUNNING_ID:
        fieldtype_models = TypeRunningId.objects.filter(field_name=field_model)
    elif field_model.field_type == DocIdTemplateTypes.SEQUENCE:
        fieldtype_models = TypeSequence.objects.filter(field_name=field_model)
    elif field_model.field_type == DocIdTemplateTypes.MAP:
        fieldtype_models = TypeMap.objects.filter(field_name=field_model)
    elif field_model.field_type == DocIdTemplateTypes.TREE:
        fieldtype_models = TypeTree.objects.filter(field_name=field_model)
    else:
        fieldtype_models = []

    for fieldtype_model in fieldtype_models:
        fields_dict['values'].append(fieldtype_model.to_dict())

    return fields_dict


def docid_get_field_values_by_docid(docid):
    db_field_values = DocIdFieldValue.objects.filter(docid=docid)
    result = {'docid':docid}
    for field_value in db_field_values:
        result[field_value.field_id.field_name] = field_value.value
    return result