# Generated by Django 4.0.1 on 2022-05-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
