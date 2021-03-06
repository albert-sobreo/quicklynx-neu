# Generated by Django 2.2.6 on 2019-11-10 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20191106_0955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='fileloc',
            new_name='file_loc',
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_no',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='semester',
            field=models.CharField(choices=[('SUMMER', 'Summer'), ('SECOND', '2nd Semeseter'), ('FIRST', '1st Semester')], default='1st Semester', max_length=25),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterModelTable(
            name='lecture',
            table=None,
        ),
    ]
