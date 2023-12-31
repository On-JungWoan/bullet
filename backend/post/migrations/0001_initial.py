# Generated by Django 4.2.3 on 2023-10-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('interval_minutes', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('url', models.CharField(max_length=200, unique=True)),
                ('site', models.CharField(max_length=200)),
                ('keyword', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
