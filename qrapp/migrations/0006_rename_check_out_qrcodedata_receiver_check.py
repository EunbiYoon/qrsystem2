# Generated by Django 3.2.12 on 2023-06-27 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0005_rename_created_at_qrcodedata_arriving_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qrcodedata',
            old_name='check_out',
            new_name='receiver_check',
        ),
    ]
