# Generated by Django 4.2.7 on 2024-01-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0004_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default='user', max_length=100),
            preserve_default=False,
        ),
    ]