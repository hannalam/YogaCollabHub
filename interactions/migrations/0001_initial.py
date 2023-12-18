# Generated by Django 4.2.7 on 2023-12-16 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('session', '__first__'),
        ('users', '0003_tutor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('interaction_date', models.DateTimeField()),
                ('liked_by_user', models.ManyToManyField(blank=True, to='users.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_interactions', to='users.profile')),
                ('yoga_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.yogaclass')),
            ],
        ),
    ]
