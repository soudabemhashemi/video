# Generated by Django 2.1 on 2021-07-28 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curl_video', '0005_auto_20210728_0638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='sub_category_name',
            new_name='sub_category_id',
        ),
    ]