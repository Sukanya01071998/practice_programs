# Generated by Django 4.0.3 on 2022-04-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='branch',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
