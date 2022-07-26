# Generated by Django 4.0.6 on 2022-07-19 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_rename_instructor_instructors_name_and_more'),
        ('Quizzes', '0002_alter_questionbank_op1_alter_questionbank_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quizattempts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment', models.CharField(max_length=10)),
                ('attempted', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.courses')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.students')),
            ],
        ),
    ]
