# Generated by Django 4.2.4 on 2023-09-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('C', 'COMPLETED'), ('P', 'PENDING')], max_length=2),
        ),
    ]
