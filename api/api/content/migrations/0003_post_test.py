# Generated by Django 2.1.3 on 2018-11-24 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20181124_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test',
            field=models.TextField(blank=True),
        ),
    ]
