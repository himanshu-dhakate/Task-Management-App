# Generated by Django 5.0.2 on 2024-02-23 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trelloapp', '0003_rename_first_name_tasks_name_remove_tasks_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateField(),
        ),
    ]
