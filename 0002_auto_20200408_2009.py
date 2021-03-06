# Generated by Django 3.0.3 on 2020-04-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='applied',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='course',
            name='certified',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='course',
            name='rating',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='course',
            name='website',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='course',
            name='length',
            field=models.CharField(default='', max_length=128),
        ),
    ]
