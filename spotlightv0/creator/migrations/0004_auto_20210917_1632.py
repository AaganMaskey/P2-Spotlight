# Generated by Django 3.2.3 on 2021-09-17 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0003_auto_20210917_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator_basic',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='creator_fund',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
