# Generated by Django 4.2.4 on 2023-08-30 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default=5, max_length=200),
            preserve_default=False,
        ),
    ]