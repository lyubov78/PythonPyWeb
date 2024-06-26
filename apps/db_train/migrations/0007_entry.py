# Generated by Django 4.2.5 on 2024-03-29 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_train', '0006_delete_entry_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='db_train.author')),
            ],
        ),
    ]
