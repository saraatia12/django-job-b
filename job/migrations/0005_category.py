# Generated by Django 3.1 on 2020-09-01 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20200831_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
