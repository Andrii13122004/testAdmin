# Generated by Django 5.1.6 on 2025-02-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0004_remove_fileupload_image1_remove_fileupload_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
