# Generated by Django 4.1.7 on 2023-02-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
