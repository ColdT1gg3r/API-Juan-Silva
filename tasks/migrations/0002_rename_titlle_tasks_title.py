# Generated by Django 5.0.6 on 2024-06-25 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='titlle',
            new_name='title',
        ),
    ]
