from django.db import models
from django.contrib.auth.models import User, Group
import json

# Create your models here.


class DocIdTemplate(models.Model):
    name = models.CharField(max_length=50)
    short_form = models.CharField(max_length=100)
    long_form = models.CharField(max_length=100)
    description = models.TextField()

    def to_json(self):
        template_dict = {
            'name': self.name, 'short_form':self.short_form, 'long_form':self.long_form,
            'description': self.description
        }
        return json.dumps(template_dict)


class DocIdTemplateTypes:
    SEQUENCE = 'SEQUENCE'
    MAP = 'MAP'
    TREE = 'TREE'
    CONSTANT = 'CONSTANT'
    RUNNING_ID = 'RUNNING_ID'


class DocIdTemplateField(models.Model):
    TYPES = (
        (DocIdTemplateTypes.SEQUENCE, DocIdTemplateTypes.SEQUENCE),
        (DocIdTemplateTypes.MAP, DocIdTemplateTypes.MAP),
        (DocIdTemplateTypes.TREE, DocIdTemplateTypes.TREE),
        (DocIdTemplateTypes.CONSTANT, DocIdTemplateTypes.CONSTANT),
        (DocIdTemplateTypes.RUNNING_ID, DocIdTemplateTypes.RUNNING_ID),
    )
    field_name = models.CharField(max_length=50, unique=True)
    field_type = models.CharField(max_length=15, choices=TYPES, null=False, blank=False,
                                  default=DocIdTemplateTypes.CONSTANT)
    description = models.TextField()

    def to_dict(self):
        ob_dict = {'field_name': self.field_name, 'field_type':self.field_type, 'description':self.description}
        return ob_dict

    def to_json(self):
        return json.dumps(self.to_dict())


class DocIdFieldValue(models.Model):
    docid = models.CharField(max_length=100, null=False)
    field_id = models.ForeignKey(DocIdTemplateField, on_delete=models.SET_NULL, null=True)
    template_id = models.ForeignKey(DocIdTemplate, on_delete=models.SET_NULL, null=True)
    value = models.CharField(max_length=50)



class TypeConstant(models.Model):
    field_name = models.ForeignKey(DocIdTemplateField, on_delete=models.SET_NULL, null=True)
    value = models.CharField(max_length=50)

    def to_dict(self):
        ob_dict = {'value': self.value}
        return ob_dict

    def to_json(self):
        return json.dumps(self.to_dict())


class TypeSequence(models.Model):
    field_name = models.ForeignKey(DocIdTemplateField, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    value = models.CharField(max_length=50)

    def to_dict(self):
        ob_dict = {'position': self.position, 'value': self.value, }
        return ob_dict


    def to_json(self):
        return json.dumps(self.to_dict())

class TypeMap(models.Model):
    field_name = models.ForeignKey(DocIdTemplateField, on_delete=models.SET_NULL, null=True)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=200)

    def to_dict(self):
        ob_dict = {'key': self.key, 'value': self.value, }
        return ob_dict

    def to_json(self):
        return json.dumps(self.to_dict())


class TypeTree(models.Model):
    field_name = models.ForeignKey(DocIdTemplateField, on_delete=models.SET_NULL, null=True)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=200)
    parent_key = models.CharField(max_length=50, null=True)

    def to_dict(self):
        ob_dict = {'key': self.key, 'value': self.value, 'parent_key': self.parent_key}
        return ob_dict

    def to_json(self):
        return json.dumps(self.to_dict())


class TypeRunningId(models.Model):
    field_name = models.ForeignKey(DocIdTemplateField, on_delete=models.SET_NULL, null=True)
    fields_list = models.CharField(max_length=500)
    digits_number = models.IntegerField(default=4)

    def to_dict(self):
        ob_dict = {'fields_list': self.fields_list, 'digits_number': self.digits_number}
        return ob_dict

    def to_json(self):
        return json.dumps(self.to_dict())

