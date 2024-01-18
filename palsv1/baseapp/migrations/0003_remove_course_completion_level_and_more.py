# Generated by Django 4.1.1 on 2023-12-07 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_course_completion_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='completion_level',
        ),
        migrations.AddField(
            model_name='subunit',
            name='question_completion_level',
            field=models.IntegerField(default=0),
        ),
    ]
