# Generated by Django 2.0.2 on 2018-03-10 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docid', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('creation_date', models.DateField()),
                ('submission_date', models.DateField()),
                ('doc_date', models.DateField()),
                ('doc', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=200)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentStatus',
            fields=[
                ('status', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='documententity',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docweb.DocumentStatus'),
        ),
    ]