# Generated by Django 5.0.2 on 2024-02-23 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trelloapp', '0007_alter_tasks_my_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='my_date',
        ),
    ]