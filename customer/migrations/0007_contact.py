# Generated by Django 3.1.6 on 2021-02-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_custinfo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=2000)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]