# Generated by Django 3.1.14 on 2022-02-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0010_auto_20220221_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listmodel',
            name='Description',
            field=models.CharField(max_length=1000),
        ),
    ]
