# Generated by Django 5.2 on 2025-04-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyprogram',
            name='program_name',
            field=models.TextField(max_length=100),
        ),
    ]
