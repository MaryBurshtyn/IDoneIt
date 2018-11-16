# Generated by Django 2.1.2 on 2018-11-20 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20181120_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='create_issue',
            field=models.BooleanField(default=0, verbose_name='create issue'),
        ),
        migrations.AlterField(
            model_name='role',
            name='create_meeting',
            field=models.BooleanField(default=0, verbose_name='create meeting'),
        ),
        migrations.AlterField(
            model_name='role',
            name='delete_issue',
            field=models.BooleanField(default=0, verbose_name='delete issue'),
        ),
        migrations.AlterField(
            model_name='role',
            name='delete_meeting',
            field=models.BooleanField(default=0, verbose_name='delete meeting'),
        ),
        migrations.AlterField(
            model_name='role',
            name='edit_issue',
            field=models.BooleanField(default=0, verbose_name='edit issue'),
        ),
        migrations.AlterField(
            model_name='role',
            name='edit_meeting',
            field=models.BooleanField(default=0, verbose_name='edit meeting'),
        ),
        migrations.AlterField(
            model_name='role',
            name='edit_project',
            field=models.BooleanField(default=0, verbose_name='edit project'),
        ),
    ]
