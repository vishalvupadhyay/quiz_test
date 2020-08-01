# Generated by Django 3.0.7 on 2020-08-01 08:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20200731_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default=None, max_length=100)),
                ('question', models.TextField()),
                ('selectedOption', models.TextField()),
                ('correctAnswer', models.TextField()),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]