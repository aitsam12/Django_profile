# Generated by Django 3.0.7 on 2020-06-28 01:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200628_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='Service name'),
            preserve_default=False,
        ),
    ]
