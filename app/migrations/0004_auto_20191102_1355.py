# Generated by Django 2.2.6 on 2019-11-02 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191102_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='verified',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='semester',
            field=models.CharField(choices=[('FIRST', '1st Semester'), ('SUMMER', 'Summer'), ('SECOND', '2nd Semeseter')], default='1st Semester', max_length=25),
        ),
    ]
