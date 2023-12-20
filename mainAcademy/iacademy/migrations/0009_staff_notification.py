# Generated by Django 4.2.6 on 2023-12-12 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iacademy', '0008_alter_subject_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iacademy.staff')),
            ],
        ),
    ]
