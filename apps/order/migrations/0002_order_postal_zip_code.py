# Generated by Django 3.1.7 on 2022-05-17 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='postal_zip_code',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
