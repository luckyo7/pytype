# Generated by Django 4.0.4 on 2022-05-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pietype', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]