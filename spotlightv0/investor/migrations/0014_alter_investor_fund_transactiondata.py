# Generated by Django 3.2.3 on 2021-09-22 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0013_investor_fund_transactiondata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor_fund',
            name='transactiondata',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
