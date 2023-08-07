# Generated by Django 4.2.3 on 2023-08-07 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='keyword',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='site',
            field=models.CharField(max_length=200),
        ),
    ]
