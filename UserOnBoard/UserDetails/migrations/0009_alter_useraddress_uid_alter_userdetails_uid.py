# Generated by Django 4.1.7 on 2023-03-30 16:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0008_alter_useraddress_uid_alter_userdetails_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('6a679351-1f6d-4d96-8be5-65cf86bdb3c3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('6a679351-1f6d-4d96-8be5-65cf86bdb3c3'), editable=False, primary_key=True, serialize=False),
        ),
    ]