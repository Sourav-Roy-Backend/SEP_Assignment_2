# Generated by Django 4.2.4 on 2023-08-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
