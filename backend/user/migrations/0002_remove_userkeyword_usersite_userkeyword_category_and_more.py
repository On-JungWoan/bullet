# Generated by Django 4.2.3 on 2023-10-15 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userkeyword',
            name='usersite',
        ),
        migrations.AddField(
            model_name='userkeyword',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='service.category'),
        ),
        migrations.AddField(
            model_name='userkeyword',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
