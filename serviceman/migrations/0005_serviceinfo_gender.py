# Generated by Django 3.1.6 on 2021-02-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceman', '0004_auto_20210215_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceinfo',
            name='gender',
            field=models.CharField(default='none', max_length=15),
        ),
    ]
