# Generated by Django 3.1.4 on 2021-01-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0002_auto_20210103_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]
