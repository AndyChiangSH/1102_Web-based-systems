# Generated by Django 3.2.12 on 2022-04-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='byear',
            field=models.IntegerField(default=2022, max_length=4),
        ),
    ]