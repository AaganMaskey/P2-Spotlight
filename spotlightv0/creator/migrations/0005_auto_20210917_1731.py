# Generated by Django 3.2.3 on 2021-09-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0004_auto_20210917_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator_basic',
            name='image',
            field=models.ImageField(default='', upload_to='static/img'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='creator_basic',
            name='category',
            field=models.CharField(choices=[('1', 'Art'), ('2', 'Technology'), ('3', 'Fasion'), ('4', 'Food'), ('5', 'Photography'), ('6', 'Others')], max_length=1),
        ),
    ]