# Generated by Django 5.0.4 on 2024-04-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetGuru', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='private_key',
            field=models.CharField(default='12', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appuser',
            name='email_address',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]