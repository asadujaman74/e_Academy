# Generated by Django 4.2.6 on 2023-11-14 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iacademy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session_Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start', models.CharField(max_length=100)),
                ('session_end', models.CharField(max_length=100)),
            ],
        ),
    ]