# Generated by Django 3.0.8 on 2020-07-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymusic', '0002_auto_20200714_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='album',
            old_name='birthday',
            new_name='released',
        ),
    ]
