# Generated by Django 2.1 on 2021-07-28 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curl_video', '0004_auto_20210727_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('sub_category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='video',
            name='category_name',
        ),
        migrations.AlterField(
            model_name='video',
            name='sub_category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_videos', to='curl_video.CategoryCatalog'),
        ),
    ]