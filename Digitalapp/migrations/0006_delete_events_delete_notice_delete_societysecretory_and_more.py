# Generated by Django 4.2.1 on 2023-05-23 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Digitalapp', '0005_alter_watchmen_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.DeleteModel(
            name='Notice',
        ),
        migrations.DeleteModel(
            name='SocietySecretory',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='member',
        ),
        migrations.DeleteModel(
            name='Watchmen',
        ),
        migrations.DeleteModel(
            name='visitor',
        ),
    ]
