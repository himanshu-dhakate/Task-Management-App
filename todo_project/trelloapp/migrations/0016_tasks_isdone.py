# Generated by Django 5.0.2 on 2024-02-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trelloapp', '0015_alter_tasks_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]
