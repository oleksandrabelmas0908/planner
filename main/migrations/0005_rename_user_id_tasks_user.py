# Generated by Django 5.1.7 on 2025-03-19 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_tasks_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='user_id',
            new_name='user',
        ),
    ]
