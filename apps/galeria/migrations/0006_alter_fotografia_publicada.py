# Generated by Django 5.0 on 2023-12-28 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_fotografia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=True),
        ),
    ]
