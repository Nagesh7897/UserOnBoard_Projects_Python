# Generated by Django 4.1.7 on 2023-03-30 16:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0002_alter_useraddress_uid_alter_userdetails_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='uid',
            field=models.UUIDField(default=uuid.UUID, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='uid',
            field=models.UUIDField(default=uuid.UUID, editable=False, primary_key=True, serialize=False),
        ),
    ]
