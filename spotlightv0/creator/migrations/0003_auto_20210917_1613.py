# Generated by Django 3.1.13 on 2021-09-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0002_auto_20210917_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creator_basic',
            name='email',
        ),
        migrations.AlterField(
            model_name='creator_basic',
            name='category',
            field=models.CharField(choices=[('1', 'Opt 1'), ('2', 'Op 2'), ('3', 'Opt 3')], max_length=1),
        ),
        migrations.AlterField(
            model_name='creator_basic',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
