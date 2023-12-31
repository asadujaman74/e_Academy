# Generated by Django 4.2.6 on 2023-11-27 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iacademy', '0005_alter_staff_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iacademy.course')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iacademy.staff')),
            ],
        ),
    ]
