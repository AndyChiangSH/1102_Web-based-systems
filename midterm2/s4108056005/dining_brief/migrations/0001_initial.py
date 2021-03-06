# Generated by Django 3.1.2 on 2022-05-03 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=10)),
                ('type', models.CharField(choices=[('T', 'Taiwanese'), ('J', 'Japanese'), ('K', 'Korean'), ('E', 'European')], max_length=1)),
                ('store_name', models.CharField(max_length=20)),
                ('like', models.BooleanField(default=True)),
                ('content', models.TextField(max_length=100)),
                ('pub_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
