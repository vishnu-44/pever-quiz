# Generated by Django 3.1.2 on 2020-10-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20201028_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
