# Generated by Django 3.2.5 on 2021-07-21 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_company_company_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='company',
        ),
    ]
