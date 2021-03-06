# Generated by Django 2.1.2 on 2018-11-27 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20181127_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='created_by',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='subject',
            field=models.CharField(error_messages={'unique': 'A meeting with that subject already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='subject'),
        ),
    ]
