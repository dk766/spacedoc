from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class DocIdTemplate(models.Model):
    name = models.CharField(max_length=50)
    short_form = models.CharField(max_length=100)
    long_form = models.CharField(max_length=100)
    description = models.TextField()


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
    field_name = models.CharField(max_length=50)
    field_type = models.CharField(max_length=15, choices=TYPES, null=False, blank=False,
                                  default=DocIdTemplateTypes.CONSTANT)
    description = models.TextField()


class TypeConstant(models.Model):
    field_name = models.ForeignKey(DocIdTemplateField, on_delete=models.SET_NULL, null=True)
    value = models.CharField(max_length=50)


class TypeSequence(models.Model):
    field_name = models.ForeignKey(DocIdTemplateField, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    value = models.CharField(max_length=50)


class TypeMap(models.Model):
    field_name = models.ForeignKey(DocIdTemplateField, on_delete=models.SET_NULL, null=True)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=200)


class TypeTree(models.Model):
    field_name = models.ForeignKey(DocIdTemplateField, on_delete=models.SET_NULL, null=True)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=200)
    parent_key = models.CharField(max_length=50, null=True)


class TypeRunningId(models.Model):
    field_name = models.ForeignKey(DocIdTemplateField, on_delete=models.SET_NULL, null=True)
    fields_list = models.CharField(max_length=500)
    digits_number = models.IntegerField(default=4)


class RunningIds(models.Model):
    running_id = models.ForeignKey(TypeRunningId, on_delete=models.SET_NULL, null=True)
    template_id = models.ForeignKey(DocIdTemplate, on_delete=models.SET_NULL, null=True)
    fields_list_value = models.CharField(max_length=500)
    running_id_value = models.IntegerField(default=0)