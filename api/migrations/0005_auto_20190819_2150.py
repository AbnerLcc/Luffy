# Generated by Django 2.2.2 on 2019-08-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190819_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='attachment_path',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='课件路径'),
        ),
    ]