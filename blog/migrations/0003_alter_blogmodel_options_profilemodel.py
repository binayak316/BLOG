# Generated by Django 4.0.6 on 2022-08-07 08:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_remove_blogmodel_updated_at_blogmodel_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'ordering': ('-created_at',)},
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='blog/images/profile', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
