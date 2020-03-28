# Generated by Django 3.0.4 on 2020-03-27 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('last_name', models.CharField(default=None, max_length=255)),
                ('pseudo', models.CharField(default=None, max_length=255)),
                ('email', models.CharField(default=None, max_length=255)),
                ('job', models.CharField(default=None, max_length=255)),
                ('password', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=255)),
                ('content', models.TextField(default=None)),
                ('publishing_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=250)),
                ('content', models.TextField(default=None)),
                ('publishing_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Users')),
            ],
        ),
    ]
