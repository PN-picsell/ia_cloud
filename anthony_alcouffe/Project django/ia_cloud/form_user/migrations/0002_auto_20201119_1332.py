# Generated by Django 3.1 on 2020-11-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='firstname',
            field=models.CharField(max_length=200),
        ),
    ]
