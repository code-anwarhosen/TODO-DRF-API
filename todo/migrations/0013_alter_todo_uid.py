# Generated by Django 4.0.3 on 2022-11-24 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(blank=True, editable=False, unique=True),
        ),
    ]
