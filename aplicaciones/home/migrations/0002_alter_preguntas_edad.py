# Generated by Django 3.2.6 on 2021-08-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntas',
            name='edad',
            field=models.IntegerField(null=True),
        ),
    ]
