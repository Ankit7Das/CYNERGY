# Generated by Django 3.1.6 on 2021-02-19 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0018_auto_20210218_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.CharField(max_length=150)),
                ('serviceman_email', models.CharField(default='none', max_length=150)),
            ],
        ),
    ]