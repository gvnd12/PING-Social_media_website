# Generated by Django 5.0.6 on 2024-07-02 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_notification_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='post_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.post'),
        ),
    ]