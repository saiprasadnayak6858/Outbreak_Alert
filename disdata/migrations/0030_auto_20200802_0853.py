# Generated by Django 3.0.7 on 2020-08-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disdata', '0029_auto_20200728_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='msg_head',
            field=models.CharField(max_length=255),
        ),
    ]
