# Generated by Django 4.0.6 on 2022-07-17 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0003_rename_instructor_instructors_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment', models.CharField(max_length=10)),
                ('weightage', models.FloatField(verbose_name='Weightage of assessment')),
                ('question', models.CharField(max_length=10)),
                ('marks', models.IntegerField(verbose_name='Maximum marks for question')),
                ('op1', models.CharField(max_length=5000, verbose_name='Option 1')),
                ('op2', models.CharField(max_length=500, verbose_name='Option 2')),
                ('op3', models.CharField(blank=True, max_length=500, null=True, verbose_name='Option 3')),
                ('op4', models.CharField(blank=True, max_length=500, null=True, verbose_name='Option 4')),
                ('ans', models.CharField(max_length=500, verbose_name='Answer')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.courses')),
            ],
        ),
    ]
