# Generated by Django 4.2.1 on 2023-06-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_rename_competition_competitionrecord_competition_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='riddle',
            name='riddle_image_id',
            field=models.CharField(default='', max_length=100, verbose_name='谜语图片id'),
        ),
    ]
