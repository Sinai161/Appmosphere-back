# Generated by Django 5.0.6 on 2024-05-24 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmosphere_app', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=300)),
                ('comment', models.CharField(max_length=500)),
                ('user', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]
