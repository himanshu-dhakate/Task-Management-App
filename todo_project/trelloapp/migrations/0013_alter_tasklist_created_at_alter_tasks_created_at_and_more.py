# Generated by Django 5.0.2 on 2024-02-26 07:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trelloapp', '0012_tasks_task_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='created_at',
            field=models.DateField(default=datetime.date(2024, 2, 26)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateField(default=datetime.date(2024, 2, 26)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='priority',
            field=models.CharField(blank=True, choices=[('High', 'high'), ('Medium', 'medium'), ('Low', 'low')], max_length=20, null=True),
        ),
    ]