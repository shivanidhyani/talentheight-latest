# Generated by Django 3.2 on 2021-04-24 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='channelcategory',
            name='icon',
            field=models.ImageField(default=12, height_field=100, upload_to='category', width_field=100),
            preserve_default=False,
        ),
    ]