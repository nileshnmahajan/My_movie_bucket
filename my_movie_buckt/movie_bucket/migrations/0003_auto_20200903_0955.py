# Generated by Django 2.2.3 on 2020-09-03 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_bucket', '0002_auto_20200903_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_bucket',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
