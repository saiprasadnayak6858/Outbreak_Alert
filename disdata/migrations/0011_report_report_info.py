# Generated by Django 3.0.7 on 2020-07-18 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disdata', '0010_auto_20200718_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_info',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
