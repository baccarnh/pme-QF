# Generated by Django 3.0.4 on 2020-03-20 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='job',
            field=models.CharField(default='', max_length=255),
        ),
    ]
