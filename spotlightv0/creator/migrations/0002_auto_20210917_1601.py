# Generated by Django 3.1.13 on 2021-09-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator_basic',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='creator_fund',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
