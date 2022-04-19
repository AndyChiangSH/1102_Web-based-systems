# Generated by Django 3.2.12 on 2022-04-12 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField(default='http://mobiles.com')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilemarket.maker')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='暱稱', max_length=15)),
                ('description', models.TextField(default='無')),
                ('year', models.PositiveIntegerField(default=2022)),
                ('price', models.PositiveIntegerField(default=0)),
                ('pmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilemarket.pmodel', verbose_name='型號')),
            ],
        ),
        migrations.CreateModel(
            name='PPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='圖片', max_length=20)),
                ('url', models.URLField(default='http://mobiles.com')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilemarket.product')),
            ],
        ),
    ]
