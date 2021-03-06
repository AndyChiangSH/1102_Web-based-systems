# Generated by Django 3.1.2 on 2022-05-03 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=10)),
                ('discription', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StoreInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=20)),
                ('avg_price', models.CharField(choices=[('1', '0~100'), ('2', '100~300'), ('3', '300~800'), ('4', 'above 800')], max_length=1)),
                ('rating', models.IntegerField()),
                ('position', models.CharField(max_length=50)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_recommendation.storetype')),
            ],
        ),
        migrations.CreateModel(
            name='FoodName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_recommendation.storeinfo')),
            ],
        ),
    ]
