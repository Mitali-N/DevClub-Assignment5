# Generated by Django 4.0.6 on 2022-07-17 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionbank',
            name='op1',
            field=models.CharField(max_length=500, verbose_name='Option 1'),
        ),
        migrations.AlterField(
            model_name='questionbank',
            name='question',
            field=models.CharField(max_length=5000),
        ),
    ]
