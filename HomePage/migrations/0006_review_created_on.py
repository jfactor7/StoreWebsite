# Generated by Django 3.1.4 on 2021-01-04 02:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0005_auto_20210103_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
