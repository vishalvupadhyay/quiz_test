# Generated by Django 3.0.7 on 2020-07-31 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='opt3',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='opt4',
            field=models.TextField(null=True),
        ),
    ]
