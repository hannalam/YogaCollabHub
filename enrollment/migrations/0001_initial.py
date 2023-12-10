# Generated by Django 4.2.4 on 2023-12-08 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('session', '0001_initial'),
        ('users', '0003_tutor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.yogaclass')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
