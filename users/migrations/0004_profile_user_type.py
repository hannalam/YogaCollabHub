# Generated by Django 4.2.7 on 2024-02-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('student', 'Student User'), ('tutor', 'Tutor User')], default='student', max_length=10),
        ),
    ]