# Generated by Django 5.1.6 on 2025-02-18 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='name',
        ),
        migrations.AddField(
            model_name='fileupload',
            name='first_name',
            field=models.CharField(default='Невідомо', max_length=100, verbose_name="Ім'я"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fileupload',
            name='last_name',
            field=models.CharField(default='Невідомо', max_length=100, verbose_name='Прізвище'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fileupload',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='По батькові'),
        ),
    ]
