# Generated by Django 4.0.6 on 2022-08-08 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_alter_profilemodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='bio',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profilemodel', to=settings.AUTH_USER_MODEL),
        ),
    ]
