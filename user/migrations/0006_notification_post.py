# Generated by Django 5.0.6 on 2024-07-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='post',
            field=models.IntegerField(default=None),
        ),
    ]