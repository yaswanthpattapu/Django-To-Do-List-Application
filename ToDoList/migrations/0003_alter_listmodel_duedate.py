# Generated by Django 4.0.2 on 2022-02-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0002_remove_listmodel_timestamp_alter_listmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listmodel',
            name='DueDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
