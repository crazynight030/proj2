# Generated by Django 3.1.7 on 2023-03-27 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardunit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
