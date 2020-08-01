# Generated by Django 3.0.7 on 2020-08-01 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_practiceresult_practicetestnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('question', models.TextField()),
                ('selectedOption', models.TextField()),
                ('correctAnswer', models.TextField()),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('practiceTestNumber', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='PracticeResult',
        ),
    ]
