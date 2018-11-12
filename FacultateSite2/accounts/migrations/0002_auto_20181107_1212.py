# Generated by Django 2.1 on 2018-11-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='facebook_site',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profesor',
            name='linkedin_site',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profesor',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='profesor',
            name='research_gate_profile',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='facebook_site',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='linkedin_site',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]
