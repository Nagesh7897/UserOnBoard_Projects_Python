# Generated by Django 4.1.7 on 2023-03-31 04:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('UserDetails', '0014_alter_useraddress_uid_alter_userdetails_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('713c0114-ab57-445a-8bee-8d1f333206f6'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('44cae5a3-8f08-4619-858b-873167730036'), editable=False, primary_key=True, serialize=False),
        ),
    ]
