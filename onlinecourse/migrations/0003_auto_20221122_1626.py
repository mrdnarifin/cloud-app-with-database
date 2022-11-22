# Generated by Django 3.1.3 on 2022-11-22 16:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20221122_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='lesson',
        ),
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=5),
        ),
    ]
