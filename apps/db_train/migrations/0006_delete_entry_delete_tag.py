# Generated by Django 4.2.5 on 2024-03-29 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db_train', '0005_tag_entry_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
