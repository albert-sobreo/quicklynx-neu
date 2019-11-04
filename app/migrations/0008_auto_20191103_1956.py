# Generated by Django 2.2.6 on 2019-11-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20191103_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='invite_token',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='semester',
            field=models.CharField(choices=[('FIRST', '1st Semester'), ('SECOND', '2nd Semeseter'), ('SUMMER', 'Summer')], default='1st Semester', max_length=25),
        ),
    ]
