from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class DocumentStatus(models.Model):
    status = models.CharField(max_length=40, primary_key=True)
    description = models.CharField(max_length=500)


class DocumentEntity(models.Model):
    docid = models.CharField(max_length=200)
    docfields = models.CharField(max_length=200)
    status = models.ForeignKey(DocumentStatus, on_delete=models.PROTECT)  # former Approved with 1 or 0
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    creation_date = models.DateField()
    submission_date = models.DateField()
    doc_date = models.DateField()
    doc = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    template_id = models.IntegerField(default=1)
