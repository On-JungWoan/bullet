# Generated by Django 4.2.3 on 2023-08-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='siteCount',
            field=models.IntegerField(default=0),
        ),
    ]
