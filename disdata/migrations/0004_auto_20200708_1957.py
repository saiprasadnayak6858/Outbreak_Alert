# Generated by Django 3.0.7 on 2020-07-08 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disdata', '0003_auto_20200708_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pincode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disdata.Pincode'),
        ),
    ]
