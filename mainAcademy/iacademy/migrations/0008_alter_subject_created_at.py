# Generated by Django 4.2.6 on 2023-12-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iacademy', '0007_subject_created_at_subject_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
