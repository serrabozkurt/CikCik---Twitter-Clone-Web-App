# Generated by Django 2.1.4 on 2018-12-13 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20181213_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
