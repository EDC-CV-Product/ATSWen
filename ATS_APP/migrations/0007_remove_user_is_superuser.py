# Generated by Django 4.0 on 2022-06-22 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ATS_APP', '0006_alter_user_managers_remove_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
    ]
